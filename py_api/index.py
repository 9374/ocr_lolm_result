import json
import cv2
from flask import Flask, request
# ,lol_m_ocr
from  lol_m_ocr import main
# __name__：代表当前这个python文件
server = Flask(__name__)
@server.route('/',methods=['get'])
def default_index():
    res = {'message':'hahah','code':0}
    return json.dumps(res)
@server.route('/index',methods=['get','post'])
def index ():
    res = {'message':'123','code':0}
    return json.dumps(res)

@server.route('/ocr',methods=['get','post'])
def ocr():
    print(request)
    img1_file_name = request.args.get("img1")
    img2_file_name = request.values.get("img2")
    res = {}
    if( img1_file_name  and img2_file_name ):
      res =  main.main(img1_file_name,img2_file_name)
    # print(res)
    # return json.dumps(res)
    return  res
server.run(host="0.0.0.0",port=4000,debug=True)