![McTone](https://github.com/user-attachments/assets/eeebcd09-6d46-483c-b75b-bc2dd769f0be)

> Generate speech with controlled emotional tone, using ElevenLabs.

McTone demonstrates how to generate natural, emotion-driven text-to-speech by
combining descriptive prompts and audio post-processing. This technique offers
simple yet powerful control over the tone and delivery of generated speech.

**Watch the full video:** _coming soon!_

This is part of an ongoing project using AI voice generation.
Subscribe to [my YouTube channel](https://www.youtube.com/@DiogoNeves) to
follow the development and learn more about AI development!

## Overview

The project showcases a technique to generate more natural and emotional
speech using ElevenLabs by:

1. Describing the speech characteristics in the prompt, similar to writing
   a novel (e.g., "she shouted angrily")
2. Using quotes to mark the actual speech
3. Post-processing the audio to extract only the relevant parts into a
   continuous audio file without the descriptive parts

**This approach allows for simple yet powerful control over the emotional tone
and delivery of the generated speech.**

## Demo

### No tone control:

The speech is generated without descriptive prompts, resulting in flat delivery.

Play: <a href="https://github.com/DiogoNeves/mctone/raw/refs/heads/main/output/speech.mp3" target="_blank">No tone control audio</a>

### Tone control:

The speech is generated using descriptive prompts, followed by post-processing
to extract only the dialogue, showcasing controlled emotional delivery.

Play: <a href="https://github.com/DiogoNeves/mctone/raw/refs/heads/main/output/post_process.mp3" target="_blank">Post-processed audio</a>

## Requirements

- [Python](https://www.python.org/downloads/) 3.8+
- ElevenLabs API key
- [FFmpeg](https://www.ffmpeg.org/download.html) installed on your system

## Setup

1. Clone this repository:

```sh
git clone https://github.com/DiogoNeves/mctone.git
cd mctone
```

2. Install the required packages:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your ElevenLabs API key:

```
ELEVENLABS_API_KEY=your-api-key-here
```

## Usage

Run the main script:

```sh
python generate_speech_post_process.py
```

This will generate two files in the `output` directory:

- `raw.mp3`: The complete audio including the speech descriptions
- `post_process.mp3`: The final audio containing only the actual speech

> You can run `generate_speech.py` to generate simple speech, without the tone
> control.

### Files

- `generate_speech_post_process.py`: Main script to generate speech with tone
  control.
- `generate_speech.py`: Basic speech generation without tone control,
  following ElevenLabs' tutorial style.
- `list_models.py`: Utility script to list available ElevenLabs voice models
  for selection.
- `requirements.txt`: Contains the Python package dependencies needed for
  the project.

# How It Works

The technique uses a specific prompt structure to control the emotional
delivery of the speech. Let's break down the approach:

## 1. Understanding the Prompt Structure

### Scene Setting: _Sets the Emotional Stage_

**_A tech support agent slowly losing their professional composure._**

The **scene setting** provides context for the AI, establishing the emotional baseline.  
Think of this as narrating the atmosphere or mood, just like introducing a scene in a story.

### Dialogue with Emotional Descriptions: _The Heart of the Prompt_

**_"Thank you for calling tech support, how may I assist you today?"_**  
**_— she said with rehearsed cheerfulness._**

This section combines the **actual speech (in quotes)** with **descriptive emotional tags**.  
The dialogue drives the spoken content, while the emotions guide tone and delivery.

- **Dialogue:**  
  _"Have you tried turning it off and on again?"_
- **Emotion Description:**  
  _— she asked professionally._

### Full Example

```python
SPEECH_PROMPT = '''A tech support agent slowly losing their professional composure.
"Thank you for calling tech support, how may I assist you today?" - she said with rehearsed cheerfulness.
"Have you tried turning it off and on again?" - she asked professionally.
"Sir, please... just try turning it off and on!" - she exclaimed with frustration.
"JUST RESTART THE COMPUTER!" - she shouted with extreme anger.'''
```

## 2. Post-Processing

The code extracts only the text within quotes, removing the descriptive
parts.

This is done by:

- Getting character-level timestamps from ElevenLabs
- Identifying quote boundaries
- Using FFmpeg to extract and concatenate the relevant audio segments

Key components:

- `_get_ranges_to_keep()`: Identifies the time ranges of the actual speech
- `_get_speech_from_audio()`: Extracts and concatenates the relevant audio
  segments

## Contributing

Feel free to raise an issue or suggest improvements in the
[Discord server](https://discord.gg/kyy5ncWsMa).  
Subscribe to [my YouTube channel](https://www.youtube.com/@DiogoNeves)!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [ElevenLabs](https://elevenlabs.io/) for their amazing text-to-speech API
- The [FFmpeg](https://www.ffmpeg.org/) team for their powerful audio
  processing tools
