# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

# <code>
import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region, service_language = "6424fc8703a443ab9b8bf97b97d3d73c", "brazilsouth", "pt-br"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region,speech_recognition_language=service_language)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

audio_file = "TesteConversa.wav"
audio_config = speechsdk.AudioConfig(filename=audio_file)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

result = speech_recognizer.recognize_once()


# Creates an audio configuration that points to an audio file.
# Replace with your own audio filename.
audio_filename = "TesteConversa.wav"
audio_input = speechsdk.audio.AudioConfig(filename=audio_filename)

# Creates a recognizer with the given settings
speech_config.speech_recognition_language="en-US"
speech_config.request_word_level_timestamps()
speech_config.enable_dictation()
speech_config.output_format = speechsdk.OutputFormat(1)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)



# Checks result.
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
# </code>