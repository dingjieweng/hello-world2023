function setup() {
  createCanvas(600, 600);
  background(0);
  noStroke();
  fill(0, 255, 0);  
}

//the ball's location at the beginning 
var ballX = 200;
var ballY = 200;

//ball speed
var ballXV = -4;
var ballYV = 1;
//Left slider
var rectX = 10;
var rectY = 10;
//Right slider
var xPaddle = 10;
var yPaddle = 50;

//started lives
var lives = 5;

function draw() {
  background(0);  
  setText();
  setShapes();    
  bounceCheck();
  increment();
  scoreCheck();  
  
  
  
  
///paddle    
  //fill(0, 255, 255);
 // noStroke();
// rect( xPaddle, yPaddle, paddleWidth, paddleHeight );
  
  
}

function increment() {  
  ballX += ballXV;  
  ballY += ballYV;
  
  if(millis() % 1000 == 0) {
    ballXV = ballXV * 2;
  }
}

function mouseMoved() {
  rectY = mouseY;
}
function keyPressed() {
  if (keyCode === UP_ARROW) {
    yPaddle -= 10;
  } else if (keyCode === DOWN_ARROW) {
    yPaddle += 10;
  }
}



function ball(x, y) {
  ellipse(x - 2, y, 30, 30);
  ellipse(x, y, 15, 15);
}

function setShapes() {
  fill(255);
  rect(rectX, rectY, 20, 75);
  rect(xPaddle, yPaddle, 20, 75);
  ball(ballX, ballY);
}

function sliderBounce() {
  ///LeftSliderBounce
  if(rectY < ballY && rectY + 100 > ballY) {
    ballXV = ballXV * -1;
    lives += 1;
  }
    
  if(yPaddle < ballY && yPaddle + 100 > ballY) {
    ballXV = ballXV * -1;
    lives += 1;
  }
  
  
}

function wallBounce() {
  ballXV = ballXV * -1;
}

function bounceCheck() {
  if(ballY < 0 || ballY > 600) {
    ballYV = ballYV * -1;
  }
  
  if(ballX < 40 && ballXV < 0) {
    sliderBounce();
  }
  
  
//  if(ballX > 170 && ballXV > 0) {
//    sliderBounce();
 // }
  
  
  if(ballX > 600 && ballXV > 0) {
    wallBounce();
  }
  
  if(ballX < 0) {
    ballX = 600;
    lives -= 1;
  }
  
  if(ballX < 0) {
    ballX = 600;
    lives -= 1;
  }
  
}

function scoreCheck() {
  if(lives == 0) {
    noLoop();
    lives = "YOU LOSE";
  }
  
  if(lives == 50) {
    noLoop();
    lives = "YOU WIN";
  }
}

function setText() {
  textAlign(CENTER);
  textSize(22);
  text(lives, 10, 20);
}