class tablero{
  private int n;
  private int casillas[][];
  public tablero(int N){
    this.n=N;
    this.casillas=new int[n][n];
    for(int j=0;j<n;j++){
      for(int i=0;i<n;i++){
        if(i>0){
          casillas[j][i]=i*n+j+1;}
        else{
          casillas[j][i]=1+j;
        }
      }
    }
  }
  public tablero(int N,int x, int y){
    this.n=N;
    this.casillas=new int[n][n];
    /*for(int j=0;j<n;j++){
      for(int i=0;i<n;i++){
        //casillas[j][i]=0; 
      }
    }*/
    casillas[x][y]=1;
  }
  void pintaTablero(color A,color B){
    float l=(width-20)/n;
    //casillas
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
    //numeracion
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
        text(casillas[i][j],(10+l*i)+(l/4),(10+l*j)+((3*l)/4));
      }
    }
  }
}
