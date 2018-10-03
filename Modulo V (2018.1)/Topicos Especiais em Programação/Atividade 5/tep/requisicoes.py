import requests
print('Rota Profiles######################3')

# for i in range(51):
#     r = requests.get('http://127.0.0.1:8000/servidor/profiles/',
#                      headers={"Authorization": "Token 66d58ded9c2c1adf8a1e4d1dd6a2b0d86c0b3f6f"})
#     print("Requisicao " + str(i+1) + " ")
#     print(r.__str__())
#     # print(r.text, "TEXT")
#     # print(r.content, "CONTENT")
#     # print(r.status_code, "STATUS CODE")
#
print('Rota Root*************************8888')
for i in range(21):
    r = requests.get('http://127.0.0.1:8000/' )
    print("Requisicao " + str(i+1) + " ")
    print(r.__str__())
#     print(r.text, "TEXT")
#     print(r.content, "CONTENT")
#     print(r.status_code, "STATUS CODE")
