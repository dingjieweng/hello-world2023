let bug;
let bugTwo;




function setup(){
  createCanvas(400, 400);

  //for(var i = 0; i < 10; i++)
  bug = new Jitter();
  bugTwo = new Jitter();

}


function draw(){
  background(56, 56, 123);

  for (let i = 0;i<numberOfBugs; i++){
    bugs[i].move();
    bugs[i].display();
    if (i )
  }
}


// Jitter class
class Jitter{
constructor(){
    this.x = random(width);
    this.y = random(height);
    this.diameter = 100;
    this.speed = 1;
    //this.color = color(255,0,0)

}
}