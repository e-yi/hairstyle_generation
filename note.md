## 参考资料

### 1. [FaceApp](https://www.reddit.com/r/MachineLearning/comments/67umwt/d_how_does_faceapp_work/)

> I managed to produce [a few failure cases](https://imgur.com/a/itQp1) which gives away some information. You can see that they pick a square around the face and process only that part and then putting it back into the original photo. Secondly, in the last picture you can see that in some cases they do apply hand crafted textures onto the image, which becomes obvious when they fail to correctly get the orientation of the head.



### 2. [smile vector](https://twitter.com/smilevector)

一个推特账号



### 3. [OpenCV](https://www.learnopencv.com/facial-landmark-detection/)

蒙版





目标：类似[edge2cat](https://affinelayer.com/pixsrv/)可以输入线条，输出发型。

- step1：使用自动边缘检测器，生成人脸边缘，跑pix2pix
- step2：输入任何人的头像，输出光头版（？？？