tablero t;
class tablero{
  private int n;
  private int casilla[][];
  public tablero(int N){
    this.n=N;
    casilla = new int[n][n];
    for (int j=0;j<n;j++){
      for (int i=0;i<n;i++){
        casilla[j][i]=i+j;
      }
    }
  }
  void pintaTablero(color A,color B){
    float l=(width-20)/n;
    for(int j=0;j<n;j++){
      for(int i=0;i<n;i++){
        if(j%2==0){
          if(i%2==0){
            fill(A);
          }
          else{
            fill(B);
          }
        }
        else{
          if(i%2==0){
            fill(B);
          }
          else{
            fill(A);
          }
        }
        rect(10+l*i,10+l*j,l,l);
      }
    }
        for(int j=0;j<n;j++){
      for(int i=0;i<n;i++){
        if(j%2==0){
          if(i%2==0){
            fill(B);
          }
          else{
            fill(A);
          }
        }
        else{
          if(i%2==0){
            fill(A);
          }
          else{
            fill(B);
          }
        }
        textSize(l/2);
        text(casilla[j][i],(10+l*i)+(l/4),(10+l*j)+((3*l)/4));
      }
    }
  }
}


void setup(){
  size(800,800);
  t = new tablero(20);
}


void draw(){
  t.pintaTablero(color(0,0,0),color(255,255,255));
}

void busquedaTablero(int x,int y){
  int p[][]={{x+2,y+1},
  {x-2,y+1},
  {x+1,y+2},
  {x+1,y-2},
  {x+2,y-1},
  {x-2,y-1},
  {x-1,y+2},
  {x-1,y-2}};
  
  boolean validacion=true;
  for (int i=0;i<8;i++){
    if(p[i][0]>0 && p[i][0]<8){
    
    }
    
  }
}
