// Beta signup for twincan.com. The landing page's form posts here; each
// signup becomes one row in D1, and export.sh turns the rows into the CSV
// that App Store Connect imports as TestFlight testers.
//
// It stores an email, an optional name and the time. Nothing else: no IP,
// no user agent, no locale. The privacy policy promises exactly that.

// Practical, not RFC 5322: no commas, quotes or brackets in the local part,
// and a dotted domain with no empty labels. Must match index.src.html.
const EMAIL = /^[^\s@,;:\"'<>()\[\]\\]+@[a-z0-9-]+(\.[a-z0-9-]+)*\.[a-z]{2,}$/i;

export default {
  async fetch(request, env) {
    const origin = request.headers.get("origin") || "";
    const allowed = env.ALLOWED_ORIGINS.split(",").map((o) => o.trim());
    const cors = allowed.includes(origin)
      ? { "access-control-allow-origin": origin, "vary": "origin" }
      : {};
    const reply = (body, status = 200) =>
      new Response(JSON.stringify(body), {
        status,
        headers: { "content-type": "application/json", ...cors },
      });

    if (new URL(request.url).pathname !== "/beta") return reply({ ok: false, error: "Not found." }, 404);
    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: { ...cors, "access-control-allow-methods": "POST", "access-control-allow-headers": "content-type", "access-control-max-age": "86400" },
      });
    }
    if (request.method !== "POST") return reply({ ok: false, error: "Use POST." }, 405);
    // Browsers always send Origin on a cross-site POST. This keeps other sites'
    // pages from posting here; a script can forge Origin, which is why every
    // write also needs a Turnstile token.
    if (!cors["access-control-allow-origin"]) return reply({ ok: false, error: "Sign up at twincan.com." }, 403);

    const body = await request.json().catch(() => null);
    if (!body || typeof body !== "object") return reply({ ok: false, error: "Something went wrong. Please try again." }, 400);

    // The honeypot: people never see this field, form-filling bots do. Tell
    // the bot it worked so it doesn't try again, and store nothing.
    if (typeof body.website === "string" && body.website !== "") return reply({ ok: true });

    const email = String(body.email ?? "").trim().toLowerCase();
    const name = String(body.name ?? "").trim().replace(/\s+/g, " ");
    if (email.length > 254 || !EMAIL.test(email)) return reply({ ok: false, error: "Enter an email address like name@example.com." }, 400);
    if (name.length > 100) return reply({ ok: false, error: "That name is too long." }, 400);

    const check = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      body: new URLSearchParams({
        secret: env.TURNSTILE_SECRET,
        response: String(body.turnstileToken ?? ""),
      }),
      signal: AbortSignal.timeout(8000),
    }).then((r) => r.json()).catch(() => ({ success: false }));
    if (!check.success) return reply({ ok: false, error: "The robot check didn’t go through. Please try again." }, 400);

    // Signing up twice is fine and says nothing about who's already on the
    // list. A second signup that adds a name fills in a blank one.
    await env.DB.prepare(
      `INSERT INTO signups (email, name) VALUES (?1, ?2)
       ON CONFLICT(email) DO UPDATE SET name = excluded.name WHERE signups.name = '' AND excluded.name != ''`,
    ).bind(email, name).run();

    return reply({ ok: true });
  },
};
