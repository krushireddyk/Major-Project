# Comparative Analysis of Human-Driven Real-World Dashcam Accident Videos and Self-Driving Vehicle Accidents

## CSCI 7200 Major Project

This project conducts a comparative analysis between accidents involving self-driving cars and those involving traditional manually operated cars. The project involves collecting a sample of 50 real-time dash cam videos from YouTube to represent normal car accidents, and 422 reports sourced from the California DMV website specifically detailing incidents involving self-driving cars. Information extraction from dash cam videos involves utilizing various vision language models such as BLIP VQA, VQA pipeline, LLaVA chatbot, DETR RESNET (End-to-End Object Detection model with ResNet-50
backbone) for segmentation, YOLO, and DETR RESNET (EndtoEnd Object Detection model with ResNet-50 backbone) for object detection. Once the necessary information is extracted,
LaMA-2 13B model is used to generate accident descriptions. In contrast, for self-driving car accidents, information is extracted from narrative reports containing detailed descriptions. Notably, the study finds a higher accuracy in describing incidents when extracting information from real-time dash cam videos using the LLaVA chatbot compared to other vision language models. The primary objective of the project is to assess self-driving accident descriptions against conventional car accident narratives. The comparison is facilitated by employing similarity scores to identify commonalities between these two types of accident descriptions. To achieve this goal, embeddings are obtained using XLNET, Spacy, Sentence Transformers, and DistilBERT and similarity scores are computed. The findings reveal that DistilBERT outperforms other models in this comparison. However, we needmore accurate models to compare these kinds of descriptions

## These files can be used on google colab

BLIP_VQA_on_video_for_sentences_frame_by_frame.ipynb - BLIP VQA for extracting information from video, frame by frame for each second.

DETR_RESNET_object_detection_for_accident_frames.ipynb - DETR RESNET for object detection.

Extract_accident_frames_from_video.ipynb - Extract accident frames which will be used for LLava chatbot model.

Sentence_Transformer_self_driving_accident_description.ipynb - Sentence Transformer is used to compare two different kinds of accident description. It gives similarity score.

Spacy_for_sentence_similarity.ipynb - Spacy is used to get similarity scores for two different types of accident descriptions.

Using_EasyOCR_to_extract_text_from_video.ipynb - EasyOCR to extract subtitles from the video.

Visual_question_answering_for_video.ipynb - VQA pipeline from huggingface to extract information from video, frame by frame for each second.

YOLO_object_detection_on_accident_frames.ipynb - YOLO for object detection.

distilbert_sentence_similarity.ipynb - DistilBERT for sentence similarity for two different types of accident descriptions.

pytube-download-youtube-videos-from-playlist.py - Pytube for downloading videos from youtube.

xlnet_sentence_similarity.ipynb - XLNET for sentence similarity for two different types of accident descriptions.



