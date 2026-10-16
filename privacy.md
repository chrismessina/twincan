# Twincan Privacy Policy

*Effective: October 15, 2026*

Twincan is a voice-note app for exactly two people, made by Chris Messina. This policy describes what it does with your information. It is short because Twincan does very little with your information.

## What Twincan stores, and where

- **Voice notes.** Recordings you make are stored on your device. When you send one, it is saved to iCloud (CloudKit) along with its title, when it was recorded, and how long it is. When your can is strung to another person, sent notes live in a shared CloudKit zone in the inviter's iCloud account, which both of you can access. Apple encrypts CloudKit data in transit and at rest.
- **The invite link.** Accepting your invite link is what grants access to the shared zone, so send it only to the person you mean to string your can to.
- **Transcripts and titles.** Transcription and note titling happen on your device using Apple's on-device speech and language models. Transcripts are stored on your device. Twincan does not send them to iCloud; titles travel with the notes you send.
- **Your name, photo, and pronouns.** If you set a profile photo or your pronouns, they are shared with the person your can is strung to, through the same shared zone.
- **Read receipts.** When you play a received note, a timestamp is written back to the shared zone so the sender's app can show the note was heard.
- **Device backups.** Like other apps' data, what Twincan stores on your device can be included in your iPhone's backups, such as iCloud Backup, according to your settings.

## Note tools: summaries, key points, and questions

Twincan can summarize a note, list its key points, rewrite it as bullets, paraphrase it, and find the questions in it. Where that work happens depends on your setup:

- **On your device, by default.** With Apple Intelligence, the tools run on Apple's on-device model, and the note's contents stay on your iPhone.
- **With your own API key.** If you add an Anthropic, OpenAI, or OpenRouter API key in Settings, the tools run through that company instead. When you use a tool, the note's transcript is sent to it, and received notes are also sent automatically to check them for questions. For a received note, the sender's name as it appears in Twincan and, if known, their pronouns are included so the result can refer to them correctly. Audio is never sent. Your key is stored in your iPhone's keychain, is not synced, and is sent only to the company it belongs to. That company's privacy policy and terms govern what it does with what it receives, and usage is billed to your key.
- **OpenRouter passes your request on.** OpenRouter is not itself the model: it forwards the transcript to the model provider it routes to (Twincan asks for Anthropic's Claude), so both OpenRouter's and that provider's policies apply.
- **Claude, provided by Twincan.** A future version of Twincan may provide access to Claude itself, so that no key is needed. Transcripts would then be sent to Anthropic in the same way, with the usage billed to Twincan. To prove it is a genuine copy of Twincan, your iPhone would use Apple's App Attest, which creates a key for this installation of the app; it identifies the installation, not your name or Apple ID. Your own key always takes precedence.
- **Connecting OpenRouter.** In versions of Twincan that offer it, you can connect an OpenRouter account instead of pasting a key. You sign in on openrouter.ai, and OpenRouter returns a one-time code to Twincan through a page on twincan.com. The page forwards the code to the app and keeps nothing; like any web page, its host may log the request. The code is useless without a secret the app sends only to OpenRouter, which exchanges the two for a key that is kept like any other.
- **Results stay on your device.** Summaries, key points, and the other results are stored on your iPhone and are not sent to iCloud.

## What Twincan does NOT do

- No accounts. Twincan uses your existing iCloud identity; we never see your password, email, or phone number.
- No servers of ours. Twincan has no backend. Your data moves through Apple's iCloud infrastructure under your own Apple ID and, only if you set up the note tools as described above, to the AI company you chose.
- No analytics, tracking, advertising, or telemetry of any kind.
- No access to your contacts database. Choosing an invite recipient uses Apple's out-of-process contact picker; Twincan keeps only the name of the person you pick.
- No sale of your data. Twincan shares it only as this policy describes: with the person your can is strung to, and with the AI company you choose.

## Microphone and speech

Twincan requests microphone access to record voice notes, and transcribes them on your device with Apple's on-device speech model. Both happen only while you use those features. Nothing recorded or transcribed leaves your device except the notes you send, their titles, and, if you set up the note tools to use an AI company, the transcripts described above.

## Unstringing and deletion

- **Unstringing** disconnects the two of you and removes the notes you received from your device. If you sent the invite, it stops sharing your zone; if you accepted one, it removes you from the other person's zone. It does not erase notes already in iCloud: the inviter's iCloud account keeps the shared zone's contents, which the inviter can remove from their iPhone's iCloud storage settings.
- **Deleting a note** removes it from Twincan and deletes its audio, transcript, and tool results from your device; a result still being made at that moment is cleared the next time Twincan tidies up. Deleting a note you already sent does not remove it from iCloud or from the other person's device.
- **Removing your API key** in Settings deletes it from your keychain. Keychain items can outlast the app, so remove your key in Settings before deleting Twincan.
- **Deleting the app** removes the recordings, transcripts, and results stored on your device.
- **Transcripts already sent** to an AI company are subject to that company's retention policy.

## Children

Twincan is not directed at children under 13 and does not knowingly collect information from them.

## Changes

If this policy changes, the updated version will be posted at this address with a new effective date.

## Contact

Chris Messina — [chrismessina.me/contact](https://www.chrismessina.me/contact/)
