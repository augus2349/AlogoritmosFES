class punto{
  float x;
  float y;
  punto(float a,float b){
    x=a;
    y=b;
  }
  void dibuja(){
    circle(x,y,5);
  }
}
