tablero t;

void setup(){
  size(800,800);
  t = new tablero(8);
}

void draw(){
  t.pintaTablero(color(255,255,255),color(0,0,0));
}

void busquedaTablero(int x, int y){
  int p[][]={{x+2,y+1}, {x-2,y+1},
  {x+1,y+2},
  {x-1,y+2},
  {x+2,y-1},
  {x-2,y-1},
  {x+1,y-2},
  {x-1,y-2}};
 
 for (int i=0; i<8; i++){
   if((p[i][0]>0 && p[i][0]<8) && (p[i][1]>0 && p[i][1]<8)){
     if(t.casillas[p[i][0]][p[i][1]]==0){
       t.casillas[p[i][0]][p[i][1]]=t.casillas[x][y]+1;
     }
   }
 }
}
