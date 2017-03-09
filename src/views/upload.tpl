<!DOCTYPE html>
<html>
  <head>
    <title>DIY Acapella</title>
    <style>
    body { background-color: #2c2f33; }
    h1 { font-family: "Comic Sans MS", cursive, sans-serif; color: white; }
    p { font-family: "Comic Sans MS", cursive, sans-serif; color: white; font-size: 20px; }
    div { font-family: "Comic Sans MS", cursive, sans-serif; color: white; font-size: 20px; }
    form { font-family: "Comic Sans MS", cursive, sans-serif; color: white; font-size: 20px; }
    </style>
  </head>
  <body>
    <h1><u>DIY Acapella Maker</u></h1>
    <p style="font-family: "Comic Sans MS", cursive, sans-serif; color: red; font-size: 26px;">{{msg}}</p>
    <p> Upload Original Song + Instrumental </p>
    <form action="/" method="post" enctype="multipart/form-data">
        Select Original: <input type="file" name="original" />
        Select Instrumental: <input type="file" name="instrumental" />
        Choose Filename for Acapella: <input type="text" name="fn" />
        <input type="submit" value="Start upload" />
    </form>
  </body>
</html>
