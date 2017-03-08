<!DOCTYPE html>
<html>
  <head>
    <title>DIY Acapella</title>
    <style>
    body { background-color: #2c2f33; }
    h1 { font-family: "Comic Sans MS", cursive, sans-serif; color: white; }
    p { font-family: "Comic Sans MS", cursive, sans-serif; color: white; font-size: 20px; }
    div { font-family: "Comic Sans MS", cursive, sans-serif; color: white; font-size: 20px; }
    </style>
  </head>
  <body>
    <h1><u>DIY Acapella Maker</u></h1>
    <div id="regFormContainer" class="bar-colors-borders">
                    <form action="uploadImages.php" method="post" onsubmit="return validateUploadFile();" enctype="multipart/form-data" >
                        <p><input type="hidden" name="MAX_FILE_SIZE" value="100000" /></p>
                        <div class="uploadFileprompt">
                            <div class="span_left">Upload Original Track (.wav)</div>
                            <div class="span_right"><input type="file" name="txtUploadFile[]"  /></div>
                        </div>
                        <div class="uploadFileprompt">
                            <div class="span_left">Upload Original Instrumental (.wav)</div>
                            <div class="span_right"><input type="file" name="txtUploadFile[]"  /></div>
                        </div>
    </div>
  </body>
</html>
