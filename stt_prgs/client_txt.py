import io
import argparse
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


# For audio files stored locally in PC
def transcribe_file(speech_file):
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content = content)
    config = types.RecognitionConfig(
        encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16,
        #sample_rate_hertz = 16000,
        language_code = 'en-US')

    response = client.recognize(config, audio)

    for result in response.results:
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))

    with open("/Users/svinjamara/Documents/google-cloud-sdk/stt_prgs/transcript_client.txt", "w") as f:
        for result in response.results:
            f.write(result.alternatives[0].transcript)

    
        

# For audio files stored remotely in GCP
def transcribe_gcs(gcs_uri):
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri = gcs_uri)
    config = types.RecognitionConfig(
        encoding = enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz = 16000,
        language_code = 'en-US')

    response = client.recognize(config, audio)

    for result in response.results:
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))

    with open("/Users/svinjamara/Documents/google-cloud-sdk/stt_prgs/transcript_client.txt", "w") as f:
        for result in response.results:
            f.write(result.alternatives[0].transcript)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = __doc__,
        formatter_class = argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument(
        'path', help = 'File or GCS path for audio file to be recognized')
    
    args = parser.parse_args()
    
    if args.path.startswith('gs://'):
        transcribe_gcs(args.path)
    else:
        transcribe_file(args.path)
        
    
    
    
