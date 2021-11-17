int n;
punto p[];
punto pmx,pMx,pmy,pMy;

void setup() {
  size(800, 600);
  background(255);
  n=10;
  p=new punto[n];
  for (int i=0; i<n; i++) {
    p[i]=new punto(random(760)+20, random(560)+20);
  }
  
  pmx=new punto(width+10,0);
  pMx=new punto(-10,0);
  pmy=new punto(0,height+10);
  pMy=new punto(0,-10);
  for(int i=0;i<n;i++){
    if(p[i].x>pMx.x){
      pMx=p[i];
    }
    if(p[i].x>pmx.x){
      pmx=p[i];
    }
    if(p[i].x>pMy.x){
      pMy=p[i];
    }
    if(p[i].x>pmy.x){
      pmy=p[i];
    }
  }
}

void draw() {
  for (int i=0; i<n; i++) {
    fill(0);
    p[i].dibuja();
  }
}
