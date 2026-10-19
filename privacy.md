# Twincan Privacy Policy

*Effective: October 18, 2026*

Twincan is a voice-note app for exactly two people, made by Chris Messina. This policy describes what it does with your information. It is short because Twincan does very little with your information.

## What Twincan stores, and where

- **Voice notes.** Recordings you make are stored on your device. When you send one, it is saved to iCloud (CloudKit) along with its title, when it was recorded, and how long it is. When your can is strung to another person, sent notes live in a shared CloudKit zone in the inviter’s iCloud account, which both of you can access. Apple encrypts CloudKit data in transit and at rest.
- **The invite link.** Accepting your invite link is what grants access to the shared zone, so send it only to the person you mean to string your can to.
- **Transcripts and titles.** Transcription and note titling happen on your device using Apple’s on-device speech and language models. Transcripts are stored on your device. Twincan does not send them to iCloud; titles travel with the notes you send.
- **Your name, photo, and pronouns.** If you set a profile photo or your pronouns, they are shared with the person your can is strung to, through the same shared zone.
- **Read receipts.** When you play a received note, a timestamp is written back to the shared zone so the sender’s app can show the note was heard.
- **Device backups.** Like other apps’ data, what Twincan stores on your device can be included in your iPhone’s backups, such as iCloud Backup, according to your settings.

## Note tools: summaries, key points, and questions

Twincan can summarize a note, list its key points, rewrite it as bullets, paraphrase it, and find the questions in it. Where that work happens depends on your setup, in Settings under AI. [twincan.com/ai](/ai/) explains it in more detail.

- **On by default, off if you choose.** AI Features is on unless you turn it off in Settings under AI. With it off, nothing about your notes is sent to any AI company.
- **On your device.** With Apple Intelligence, the tools run on Apple’s on-device model, and the note’s contents stay on your iPhone.
- **With your own API keys.** If you add an Anthropic, Google, OpenAI, or OpenRouter API key in Settings, the tools can run through that company instead. Requests go directly from your iPhone to that company, under your own account with it. When you use a tool, the note’s transcript is sent to it, and received notes are also sent automatically to check them for questions. For a received note, the sender’s name as it appears in Twincan, limited to letters, numbers, apostrophes and hyphens and at most three words, and, if known, their pronouns are included so the result can refer to them correctly. Audio is never sent. When you verify a key, and each time you open OpenRouter’s page in Settings, Twincan sends the company a small test request that contains nothing from your notes. A tool you have open is redone automatically when its result goes out of date, for example after you change providers. Requests to OpenRouter identify Twincan as the app making them. Usage is billed to your key.
- **Several providers, in your order.** Twincan tries your providers in the order set under Provider Priority, which can include Apple Intelligence. If one can’t produce a complete result, the note’s transcript is sent to the next. Apple Intelligence is tried only if your iPhone has it, and other companies only if you’ve added a key for them, and only while you leave them switched on.
- **Each company’s terms apply.** That company’s privacy policy and terms govern what it does with what it receives. In particular, Google’s terms allow it to use content sent on its free tier to improve its products, including through human review; its paid tier does not.
- **OpenRouter passes your request on.** OpenRouter is not itself the model: it forwards the transcript to the model provider it routes to (Twincan asks for Anthropic’s Claude), so both OpenRouter’s and that provider’s policies apply.
- **Your keys.** Keys are stored in your iPhone’s keychain, are not synced, are never sent to Twincan, and are each sent only to the company they belong to.
- **Connecting OpenRouter.** You can connect an OpenRouter account instead of pasting a key. You sign in on openrouter.ai, and OpenRouter returns a one-time code to Twincan through a page on twincan.com. The page forwards the code to the app and keeps nothing; like any web page, its host may log the request. The code is useless without a secret the app sends only to OpenRouter, which exchanges the two for a key that is kept like any other.
- **Results name their source.** Results are labeled with the provider and model that produced them.
- **Results stay on your device.** Summaries, key points, and the other results are stored on your iPhone and are not shared through iCloud with your notes. Like Twincan’s other data, they can be included in your iPhone’s backups.

## What Twincan does NOT do

- No accounts. Twincan uses your existing iCloud identity; we never see your password, email, or phone number.
- No servers of ours. Twincan has no backend. Your data moves through Apple’s iCloud infrastructure under your own Apple ID and, only if you set up the note tools as described above, to the AI companies you chose.
- No analytics, tracking, advertising, or telemetry of any kind.
- No access to your contacts database. Choosing an invite recipient uses Apple’s out-of-process contact picker; Twincan keeps only the name of the person you pick.
- No sale of your data. Twincan shares it only as this policy describes: with the person your can is strung to, and with the AI companies you choose.

## Microphone and speech

Twincan requests microphone access to record voice notes, and transcribes them on your device with Apple’s on-device speech model. Both happen only while you use those features. Nothing recorded or transcribed leaves your device except the notes you send, their titles, and, if you set up the note tools to use AI companies, the transcripts described above.

## Unstringing and deletion

- **Unstringing** disconnects the two of you and removes the notes you received from your device. If you sent the invite, it stops sharing your zone; if you accepted one, it removes you from the other person’s zone. It does not erase notes already in iCloud: the inviter’s iCloud account keeps the shared zone’s contents, which the inviter can remove from their iPhone’s iCloud storage settings.
- **Deleting a note** removes it from Twincan and deletes its audio, transcript, and tool results from your device; a result still being made at that moment is cleared the next time Twincan tidies up. Deleting a note you already sent does not remove it from iCloud or from the other person’s device.
- **Removing an API key** in Settings deletes it from your keychain. Keychain items can outlast the app, so remove your keys in Settings before deleting Twincan.
- **Deleting the app** removes the recordings, transcripts, and results stored on your device.
- **Transcripts already sent** to an AI company are subject to that company’s retention policy.

## Children

Twincan is not directed at children under 13 and does not knowingly collect information from them.

## Changes

If this policy changes, the updated version will be posted at this address with a new effective date.

## Contact

Chris Messina — [chrismessina.me/contact](https://www.chrismessina.me/contact/)
