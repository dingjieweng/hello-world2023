// Making it bounce
var xBallChange = 5;
var yBallChange = 5;



//   xBall starts off the ball with a random x-coordinate between 50 and 350. yBall //   starts off the ball with a default y-coordinate of 50. The diameter is also set //   to /50.
var xBall = Math.floor(Math.random() * 300) + 50;
var yBall = 50;
var diameter = 50;


///adding a paddle
var xPaddle;
var yPaddle;
var paddleWidth = 100;
var paddleHeight = 25;

//adding another paddle
var xSlider;
var ySlider;
var sliderWidth = 100;
var sliderHeight = 25;

var started = false;



///canvas background
function setup() {
  createCanvas(windowWidth, windowHeight);
}

///draw ball
function draw() {
  
  
  background(0);
  xBall += xBallChange;
  yBall += yBallChange;
  fill(255, 0, 255);
  noStroke();
  
  ellipse(xBall, yBall, diameter, diameter);
  
  

  
  
//Walls
  if (xBall < diameter/2 || 
      xBall > windowWidth - 0.5*diameter) {
  xBallChange *= -1;
  }
if (yBall < diameter/2 || 
     yBall > windowHeight - diameter) {
  yBallChange *= -1;
   }

  
  //Detecting collision with the slider
 
  if ((xBall > xSlider &&
      xBall < xSlider + sliderWidth) &&
      (yBall + (diameter/2) >= ySlider)) {
  xBallChange *= -1;
  yBallChange *= -1;
}
  
///slider
  fill(0, 79, 255);
  noStroke();
  rect( xSlider, ySlider, sliderWidth, sliderHeight);
  

  
  
  //Detecting collision with the paddle
 
  if ((xBall > xPaddle &&
      xBall < xPaddle + paddleWidth) &&
      (yBall + (diameter/2) >= yPaddle)) {
  xBallChange *= -1;
  yBallChange *= -1;
}
 
  
///paddle    
  fill(0, 255, 255);
  noStroke();
  rect( xPaddle, yPaddle, paddleWidth, paddleHeight );

  
///set the paddle in the middle before the game starts  
if (!started) {
  xPaddle = windowWidth / 2;
  yPaddle = windowHeight - 100;
  xSlider = windowWidth / 2;
  ySlider = windowHeight - 100;
  }
  started = true;

}
  
  


///making paddle controlled by keyboard
function keyPressed() {
  if (keyCode === LEFT_ARROW) {
    xPaddle -= 50;
  } else if (keyCode === RIGHT_ARROW) {
    xPaddle += 50;
  }
  if (keyCode === CONTROL){
    xSlider -=50;
  } else if (keyCode === OPTION ){
    xSlider +=50;
}

}