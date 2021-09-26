let angles = [100,200,30,30];
let names = ["Motorbikes","Cars","Heavy Vehicles","Others"]
let probs = [0.15,0.4,0.25,0.2]
let counts = [0,0,0,0]

function preload() {
  let url = "http://127.0.0.1:5000"

  httpGet(url, 'json', false, function(response){

    count = response.total_count
    for(let i=0;i<4;i++){
      counts[i] = int(count * probs[i]) 

      angles[i] = counts[i]/count * 360
    }
  })
}

function setup() {
  createCanvas(800, 800);
  noStroke(); // Run once and stop
}

function draw() {
  background(180);
  pieChart(400, angles);
}

function pieChart(diameter, data) {
  let lastAngle = 0;
  for (let i = 0; i < data.length; i++) {
    fill(255 - 60*i,69 - 20*i,  50*i);
    arc(
      width / 2,
      height / 2,
      diameter,
      diameter,
      lastAngle,
      lastAngle + radians(angles[i])
    );
    strokeWeight(3);
    textSize(20);
    ellipse(580,590+30*i,20,20)
    fill(0,0,0);
    text(names[i] + " - " + counts[i], 600, 600 + 30*i);
    lastAngle += radians(angles[i]);
  }
}