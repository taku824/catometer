from google.cloud import vision


# import os
# credential_path = "C:\Users\augus\OneDrive\Desktop\python\vision-ai-test\nifty-stage-313710-6d11794f516f.json"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# print("user >", end="")
# input()
# print("AI >ん？")
# print("user >", end="")
# input()
# print("AI >ええで。画像URLくれ：", end="")
img_path = input()
# print("user >", end="")
# input()
# print("AI >可愛い。")
# print("user >", end="")
# input()
# print("AI >へいへい。")
# print("")

# print("解析したい画像のナンバーを00-99で入力してください：", end="")
# input = input()





# img_path = "./images/img_" + input + ".jpg"
# print(img_path)

with open(img_path, 'rb') as image_file:
	content = image_file.read()

# visionAPIが扱えるデータ形式
image = vision.Image(content=content)
# print(image)

# インスタンスを生成
annotator_client = vision.ImageAnnotatorClient()

response_data = annotator_client.label_detection(image=image)

labels = response_data.label_annotations

print('--------RESULT--------')
for label in labels:
	print(label.description, ':', round(label.score * 100, 2), '%')
print('----------------------')	