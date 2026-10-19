# Twincan and AI

Twincan can summarize a voice note, pull out its key points, rewrite it as bullets, paraphrase it, and find the questions in it. These are the note tools. This page explains where they run, what leaves your iPhone when they do, and how to use your own AI providers if you want to.

The short version: on an iPhone with Apple Intelligence and no API keys, the note tools run on the iPhone and nothing leaves it. If you add an API key from Anthropic, Google, OpenAI, or OpenRouter, the tools run through that company too, in an order you control: the note's transcript goes straight from your iPhone to it, and the usage is billed to your key. Twincan has no servers of its own, so nothing passes through Twincan on the way. You can also turn the tools off entirely.

## What the note tools do

Long-press a note, or open its transcript, and pick a tool:

| Tool | What you get |
|---|---|
| Summarize | A few sentences on what the note is about. |
| Key Points | The main points, most with a button that jumps to that moment in the audio. |
| Bullet Points | The note rewritten as a short list. |
| Paraphrase | The note said again in plainer words. |
| Extract Questions | The questions in the note, including indirect ones ("let me know if Thursday works"), most with a button to hear it. |

The tools only read. They can't send notes, change anything in your can, or act on your behalf, and their results are stored on your iPhone. They aren't shared through iCloud with your notes, though like the rest of Twincan's data they can be part of your iPhone's backups. Results usually name the provider and model that wrote them at the bottom, such as APPLE INTELLIGENCE · ON THIS IPHONE or CLAUDE SONNET 5.5 · ANTHROPIC.

## Where the tools run

Everything lives in Twincan's Settings, under **AI**:

- **AI Features** turns the note tools on or off. Off means nothing about your notes is sent to any AI provider, and the note pane shows only the transcript. (Sending a note to the other person through iCloud works as usual.)
- **Custom API Keys** is where you add a key for each provider.
- **Provider Priority** appears once you've saved a key that has been verified or needs credits. It's the order Twincan tries your providers in, with Apple Intelligence in the list if your iPhone has it.

Twincan tries the first provider in the list. If it can't produce a result (it's down, it declines the note, or the key has run out of credits), Twincan tries the next one, and so on. A provider whose key was rejected or needs credits is skipped until you fix it, and you can switch any provider off in the list without removing its key. The footer under **AI** in Settings spells out the current order in a sentence.

Unless you've moved Apple Intelligence up, a new key goes just ahead of it. If you'd rather notes stay on your iPhone whenever possible, drag Apple Intelligence to the top: a provider further down then sees a note only when Apple Intelligence can't handle it.

Without Apple Intelligence or a working key, the tools don't appear (a tool you already have open keeps its message and Try Again button). Adding a key is how you get them on an iPhone without Apple Intelligence.

## Supported providers

| Provider | Model Twincan uses | Key starts with |
|---|---|---|
| Apple Intelligence | Apple's on-device model | No key |
| [Anthropic](https://www.anthropic.com) | Claude Sonnet 5.5 | sk-ant- |
| [Google](https://ai.google.dev) | Gemini 3.8 Flash | AIza |
| [OpenAI](https://openai.com) | GPT-5.6 Terra | sk- |
| [OpenRouter](https://openrouter.ai) | Claude Sonnet 5.5, through OpenRouter | sk-or- |

Twincan chooses the model for each provider; there is no model picker. If you don't already have an account with any of these, **OpenRouter is the easiest start**: Twincan can connect to it without you copying a key at all (see below). If you already pay for Anthropic's API, use an Anthropic key, since the request then goes to one company instead of two.

## Getting an API key

An API key is a password that lets an app use your account with an AI company. It's separate from a ChatGPT, Claude, or Gemini subscription: those plans don't include API usage, which is billed on its own.

Each provider's page in Twincan (Settings → AI → Custom API Keys) has a **Manage in** button that opens the page where you make a key, in a sheet you can swipe away to get back to Twincan.

### Anthropic

1. Go to [platform.claude.com](https://platform.claude.com) and sign in, or create an account.
2. Add credits under [Billing](https://platform.claude.com/settings/billing). Keys don't work until the account can pay.
3. Open [API keys](https://platform.claude.com/settings/keys), click **Create key**, and name it "Twincan".
4. Copy the key. Anthropic shows it only once; if you lose it, make a new one.

### Google

1. Go to [Google AI Studio](https://aistudio.google.com/apikey) and sign in with your Google account.
2. Click **Create API key**. If asked, let it create a new project.
3. Copy the key.

Google's API works without billing, on a free tier with lower limits. Read the note on Google's free tier under "What providers do with it" before you choose it.

### OpenAI

1. Go to [platform.openai.com](https://platform.openai.com) and sign in, or create an account.
2. Add credits or a payment method under [Billing](https://platform.openai.com/settings/organization/billing).
3. Open [API keys](https://platform.openai.com/api-keys), click **Create new secret key**, and name it "Twincan".
4. Copy the key. OpenAI shows it only once.

### OpenRouter

You can skip the key entirely: on OpenRouter's page in Twincan, tap **Connect OpenRouter Account**, sign in on openrouter.ai, and approve Twincan. OpenRouter hands Twincan a key of its own, which is checked and stored like a pasted one. You still need credits on your OpenRouter account.

To make a key by hand instead:

1. Go to [openrouter.ai](https://openrouter.ai) and sign in, or create an account.
2. Add credits under [Credits](https://openrouter.ai/settings/credits).
3. Open [Keys](https://openrouter.ai/settings/keys) and click **Create key**. You can give it a credit limit here.
4. Copy the key.

## Adding a key to Twincan

1. Open Settings in Twincan and go to **AI → Custom API Keys**.
2. Tap the provider.
3. Paste your key into the **API Key** field.
4. Tap **Verify**.

Verify sends the provider one tiny test request (the word "Hi", nothing from your notes) to check that the key works and the account can pay for it. For OpenRouter it first looks up the key's remaining allowance, and it checks again each time you open OpenRouter's page in Settings; each of those test requests is billed like any other, though it is tiny. The key is saved only if the provider recognizes it. The provider's row then shows its status:

| Status | What it means |
|---|---|
| ✓ Verified | The key works. For OpenRouter, the page also shows how much is left on the key if it has a credit limit. |
| Needs credits | The key is real but the account can't pay. Twincan skips it until you add credits, then tap the refresh button to check again. |
| Rejected | The provider turned the key down. Paste a new one. |
| Not verified yet | A key saved by an earlier version of Twincan. It's used until a request or Verify says otherwise. |

To replace a key, paste a new one into the same field and tap Verify. To remove it, tap **Remove** at the bottom of the provider's page.

## What is sent, and when

Nothing is sent while a note runs on Apple Intelligence. When a note runs through a provider with your key, here is what leaves your iPhone:

| What | Sent? | When |
|---|---|---|
| The note's transcript, as text | Yes | When you use a tool on it |
| Received notes' transcripts | Yes | Automatically, after they arrive and while Twincan is open, to check them for questions |
| Instructions telling the model what to do | Yes | With every request |
| The sender's name as it appears in Twincan (tidied), and their pronouns if known | Yes, for received notes | With the request, so the result can refer to them correctly |
| The note's audio | Never | |
| Its title, date, or length | Never | |
| Your other notes, your photo, or your contacts | Never | |
| Anything about your iCloud account | Never | |

The sender's name is tidied before it's sent: it keeps only letters, numbers, apostrophes and hyphens, and at most three words.

Because Twincan falls back down your Provider Priority list, a note one provider couldn't handle can be sent to the next one. Apple Intelligence is tried only if your iPhone has it, and other providers only if you've added a key for them; either way, only if you've left them switched on. A result whose footer says Apple Intelligence may still have been tried elsewhere first: if Apple Intelligence produces only part of an answer, Twincan tries the next providers, and shows Apple's partial answer only if none of them does better.

Two things happen without you tapping a tool:

- **The automatic question check** runs on notes you received, and is what lets Twincan show that a note has questions waiting for you. Adding a key lets it check notes you received before.
- **A tool you have open stays current.** If its result is out of date, Twincan makes a new one when the note pane reloads.

Results are kept, so a note isn't re-sent every time you open the app. A note is sent again when its result goes out of date: after you add, remove, switch, or reorder providers, when the sender's pronouns change, when Twincan's instructions change in an update, or when an earlier try didn't finish. On Apple Intelligence all of this happens on your iPhone.

Requests go directly from your iPhone to each provider. If Google rejects the format Twincan asks for, Twincan sends the request once more in a simpler form. Requests to OpenRouter name Twincan as the app making them. OpenRouter is a router, not a model: it passes your request on to the model provider it routes to (Twincan asks it for Anthropic's Claude), so both OpenRouter's and that provider's policies apply.

### Your keys

Your keys are stored in your iPhone's keychain, the same place iOS keeps passwords. They stay on this iPhone: they aren't synced to iCloud Keychain, aren't included in a backup that can be restored to another phone, and each is sent only to the company it belongs to. Keychain items can outlast an app, so remove your keys in Settings before deleting Twincan.

### What providers do with it

What a provider does with what it receives is governed by its own terms. As of this writing, Anthropic, OpenAI, and OpenRouter say they don't train models on API data by default.

**Google's free tier is different.** Under Google's Gemini API terms, if your Google key is on the free tier, Google may use what it receives, transcripts included, to improve its products, and people may review it. Turning on billing for the key's project moves it to Google's paid terms, which don't. If that matters to you, turn on billing, or use another provider.

Check each company's current terms rather than taking our word for it:

- Anthropic: [Commercial terms](https://www.anthropic.com/legal/commercial-terms) and [Privacy policy](https://www.anthropic.com/legal/privacy)
- Google: [Gemini API terms](https://ai.google.dev/gemini-api/terms) and [Privacy policy](https://policies.google.com/privacy)
- OpenAI: [Your data](https://developers.openai.com/docs/guides/your-data) and [Privacy policy](https://openai.com/policies/privacy-policy/)
- OpenRouter: [Privacy policy](https://openrouter.ai/privacy) and [Terms](https://openrouter.ai/terms)

Twincan's own [privacy policy](/privacy/) covers all of this too.

## What it costs

Twincan doesn't charge for the note tools. With your own key, each provider bills your account for each request, by the amount of text in and out, at its standard rates. A voice note's transcript is short, so each tool is a small charge, but the automatic question check adds a request for most notes you receive, and a note can be sent to more than one provider when one falls back to the next. See each provider's pricing page for current rates.

If you want a ceiling, set a spending limit in your provider's dashboard, or a credit limit on the OpenRouter key.

## Troubleshooting

When a tool can't finish, the note shows a message and a **Try Again** button.

**"Couldn't finish just now."** Twincan couldn't get a result this time: you're offline, a provider is busy or rate-limiting you, a key stopped working, providers were skipped because they're out of credits or busy, or something went wrong saving the result. Wait a moment and tap Try Again. If it keeps happening, open Settings → AI → Custom API Keys and look for a key marked **Needs credits** or **Rejected**.

**"None of your AI providers could read this one."** Every provider that tried couldn't handle this note: a content filter declined it, it's too long, it's in a language the model doesn't support, or the answer came back unusable. Adding another provider may help.

**"Add a provider in Settings → AI."** AI Features is on, but there's nothing to run on: no Apple Intelligence and no key, or you've switched every provider off in Provider Priority.

**"Your AI providers need attention in Settings → AI."** You have providers switched on, but none can be used right now, usually because each key needs credits or was rejected.

When you tap Verify:

- **"That looks like an OpenAI key."** (or another provider) The key belongs to a different provider than the page you're on. Open that provider's page instead.
- **"Anthropic rejected this key."** (or another provider) The key was copied wrong, revoked, or expired. Make a new one.
- **"Couldn't reach Google. Try again."** (or another provider) Twincan couldn't tell whether the key works: you're offline, or the provider was busy, rate-limiting, or answered with an error. The key you pasted wasn't saved; a key saved earlier stays as it was.
- **"Google won't allow this key here."** (or the provider's own message) The provider refused the key for this use, for example because of the account's region or permissions.

**The tools don't appear.** Check that AI Features is on, and that you have Apple Intelligence turned on or a verified key. The tools also stay hidden on your draft, until a note's transcript is ready, on notes with very little speech, and in the Red Room.

## Questions

### Is my data used to train AI models?

Not by Apple Intelligence, which never sends your note anywhere. Anthropic, OpenAI, and OpenRouter each say API data isn't used for training by default. Google's free tier may use it; its paid tier doesn't. Their terms above are the final word.

### Can I use a free key?

Google's free tier works without billing, with the training caveat above. Anthropic and OpenAI require credits before a key works. OpenRouter has free models, but Twincan asks it for Claude, which is paid, so you need credits there too.

### Which should I choose?

If your iPhone has Apple Intelligence and you'd rather nothing left it, don't add a key, or put Apple Intelligence first. If you want sharper summaries or your iPhone doesn't have Apple Intelligence, Connect OpenRouter Account is the quickest way in, and an Anthropic key is the most direct. You can add more than one and let Twincan fall back between them.

## Questions or problems

Get in touch at [chrismessina.me/contact](https://www.chrismessina.me/contact/).
