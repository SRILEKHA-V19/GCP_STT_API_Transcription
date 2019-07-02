# GCP Speech-to-Text API for Transcription
*Using GCP STT(Speech to Text) API for transcription of video files(to audio) to text.*

1. Download Google Cloud SDK.

2. Open 1_procedure_startGCloud.png to see 3 commands to be executed everytime on a new terminal(for gcloud to start):

    *$ export GOOGLE_APPLICATION_CREDENTIALS=(file path to service account json file)*
  
    *$ source '(user path)/google-cloud-sdk/path.bash.inc'*
  
    *$ source '(user path)/google-cloud-sdk/completion.bash.inc'*
  
        These link us to our gcloud project successfully.

3. To run /stt_prgs/client_transcribe.py file, goto stt_prgs folder and type the following in terminal:

    *$ python client_transcribe.py (path name to the audio file)*
  
        This file is used to convert the speech stored in a local file in PC to text.
  
        Example: 2_STT_localFile.png
        
        Demo: localFile_audio_transcription_compressed.mov
  
4. To run /stt_prgs/realTime_stt.py file, goto stt_prgs folder and type the following in terminal:

    *$ python realTime_stt.py*
  
        This file is used to convert real time speech passed via microphone to text.
    
        Example: 3_STT_realTime_microphone.png
        
        Demo: realTime_audio_transcription_compressed.mov
  
5. To run /stt_prgs/video_model_transcribe.py file,goto stt_prgs folder and type the following in terminal:

    *$ ffmpeg -i <input_video_file> <output_audio_file>*
  
    *$ python video_model_transcribe.py (path name to the audio file) --model video*

6. Example_gcp_bucketFile.png is an example transcription of an audio file located in cloud bucket, accessed using gcloud uri.
 
 
# Extension of 3 & 4:
1. /stt_prgs/client_txt.py is used to store all the local file transcriptions in a .txt file in PC.

   The transcripted file is: /stt_prgs/transcript_client.txt
   
2. Similarly /stt_prgs/realTime_txt.py is used to locally store file transcriptions obtained in realtime.
