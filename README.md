# 👽📡 SETI Decrypt Challenge

This repository contains the generation and decryption code for the famous SETI Decrypt Challenge message.

## 📑 Documentation and useful links

>This is a call for a fun scientific challenge.
>
>Suppose a telescope on Earth receives a series of pulses from a fixed, unresolved source beyond the solar system. The source is a star about 50 light years from Earth. The pulses are in the form of short/long signals and they are received in a very narrow band around an electromagnetic frequency of 452.12919 MHz. A computer algorithm identifies the artificial nature of the pulses. It turns out the pulses carry a message. The pulses signify binary digits. Suppose further that you were, by whatsoever reason, put in charge of decoding this message.
>
>If you successfully decrypted the message, you should be able to answer the following questions:
>
>1. What is the typical body height of our interstellar counterparts?
>2. What is their typical lifetime?
>3. What is the scale of the devices they used to submit their message?
>4. Since when have they been communicating interstellar?
>5. What kind of object do they live on?
>6. How old is their stellar system?
>
>These are the rules.
>
>1. No restrictions on collaborations.
>2. Open discussion (social networks etc.) of possible solutions strongly encouraged.
>3. 3 hints to the solutions can be offered as per request.
>4. Send your solutions to me via e-mail (heller@mps.mpg.de), twitter (@DrReneHeller) or facebook (DrReneHeller). Human-readable format and the format of the message are allowed.
>5. On 3 June 2016, a list of the successful SETI crackers (in chronological order) will be released.

- [Tweet of the challenge with the instructions and the message to be decrypted](https://twitter.com/drreneheller/status/724935476327624704?lang=es)
- [Solution and list of 66 successful crackers](https://twitter.com/DrReneHeller/status/738711049361358849)
- [Paper of the results of the challenge](https://www.cambridge.org/core/journals/international-journal-of-astrobiology/article/decryption-of-messages-from-extraterrestrial-intelligence-using-the-power-of-social-media-the-seti-decrypt-challenge/C79C7B63CC86948D2225F1558976E284)

## 🔰 Usage

- Generate original message ([@DrReneHeller](https://twitter.com/DrReneHeller/status/872400149187887104))

```bash
python ./message-generation/SETImessage.py
```

- Decrypt message

```bash
python ./solution/decrypt-message.py
# The following commands allow to obtain the images of the message
python ./solution/generate-image.py
python ./solution/generate-separate-images.py
perl ./solution/generate-separate-images.pl
```

## 🤩 Inspiration

- [lcarpino/SETI-Decrypt-Challenge](https://github.com/lcarpino/SETI-Decrypt-Challenge)
- [ramosjoel/SETIDecryptChallenge2016](https://github.com/ramosjoel/SETIDecryptChallenge2016)
- [jgrahamc/seti.pl](https://gist.github.com/jgrahamc/e06647f41ed6d7c726fee8d1d428337f)

## ⚖️ License

The MIT License (MIT). Please see [License](LICENSE) for more information.
