# Debate This

Generate emotional speech using ElevenLabs with fine-tuned control over the output. This project demonstrates a technique to achieve more natural and emotional text-to-speech by explicitly describing the speech characteristics and post-processing the audio.

This repository contains the code demonstrated in the YouTube video: [How to Generate Emotional Speech with ElevenLabs](your-video-link-here)

## Overview

The project showcases a technique to generate more natural and emotional speech using ElevenLabs by:

1. Describing the speech characteristics in the prompt (e.g., "she shouted angrily")
2. Using quotes to mark the actual speech
3. Post-processing the audio to extract only the relevant parts

This approach allows for better control over the emotional tone and delivery of the generated speech.

## Requirements

- Python 3.8+
- ElevenLabs API key
- FFmpeg installed on your system

Python packages:

```
elevenlabs==1.11.0
ffmpeg==1.4
python-dotenv==1.0.1
pydantic==2.9.2
requests==2.32.3
```

## Setup

1. Clone this repository:

```
git clone https://github.com/yourusername/debate-this.git
cd debate-this
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your ElevenLabs API key:

```
ELEVENLABS_API_KEY=your-api-key-here
```

4. Create an `output` directory:

```
mkdir output
```

## Usage

Run the main script:

```
python generate_speech_post_process.py
```

This will generate two files in the `output` directory:

- `raw.mp3`: The complete audio including the speech descriptions
- `post_process.mp3`: The final audio containing only the actual speech

## How It Works

The technique uses a specific prompt structure to control the emotional delivery of the speech. Let's break down the approach:

1. **Prompt Structure**

```
SPEECH_PROMPT = '''The following is an argument between two people at work.
Fast pace frustration and anger, high energy.
"How dare you interrupt me while I'm working!" - she shouted angrily.
"This is absolutely ridiculous," - she expressed in frustration.
[...]'''
```

The prompt includes:

- Context setting
- Emotional state description
- Speech enclosed in quotes with explicit delivery instructions

2. **Post-Processing**
   The code extracts only the text within quotes, removing the descriptive parts. This is done by:

- Getting character-level timestamps from ElevenLabs
- Identifying quote boundaries
- Using FFmpeg to extract and concatenate the relevant audio segments

Key components:

- `_get_ranges_to_keep()`: Identifies the time ranges of the actual speech
- `_get_speech_from_audio()`: Extracts and concatenates the relevant audio segments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [ElevenLabs](https://elevenlabs.io/) for their amazing text-to-speech API
- The FFmpeg team for their powerful audio processing tools
