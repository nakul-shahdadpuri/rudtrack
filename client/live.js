let names = ["Motorbikes","Cars","Heavy Vehicles","Others"]
let probs = [0.15,0.4,0.25,0.2]
let counts = [1,1,1,1]

let car;
function preload()
{
   car = loadImage('./car.png');
   bike = loadImage('./bike.png');
   truck = loadImage('./truck.jpg');
}
function get_counts() {
  let url = "http://127.0.0.1:5000"

  httpGet(url, 'json', false, function(response){

    count = response.total_count
    for(let i=0;i<4;i++){
      counts[i] = int(count * probs[i]) 
    }
  })
}

function setup() {
  createCanvas(800, 800);
  

  i = 30
}

function draw() 
{

  background(240);
  get_counts()
  line(30,10,30,600);
  line(30,600,800,600);
  for(let z=600;z>0;z = z - 10){
    strokeWeight(5)
    text(600-z, 5 ,z + 5);
    point(30,z);
    strokeWeight(1)
  }


  for (let j=0;j<4;j++)
  {
    text(names[j] + ": ",650,650 + j * 20)
    text(counts[j],750,650 + j * 20)
  }


  image(bike,i,580-counts[0],40,40)
  line(i,580-counts[0],30,580-counts[0])
  line(i,580-counts[1],i,600)


  image(car,i,580-counts[1],40,40)
  line(i,580-counts[1],30,580-counts[1])
  line(i,580-counts[1],i,580-counts[1])


  image(truck,i,580-counts[2],40,40)
  line(i,580-counts[2],30,580-counts[2])
  line(i,580-counts[2],i,580-counts[2])

  if(i == 800){
    i = 30
  }

  i = i + 1
}

