Framework of my kMC
===========

This is a framework of my kMC code

::

      #include<stdio.h>
      #include<math.h>
      #include<stdlib.h>
      #include<vector>
      #include<time.h>
      #define N_limit 80000000
      using namespace std;
      const int multiplier=50;
      const int step_out=10000000;
      const int row=2000;
      const int col=2000;

      const int c_num=10;

      double t=0.0;
      //const int G_row=200;
      //const int G_col=200;
      const double kT=0.112;
      int num_evt[2]={0};
      int mesh[row][col][2]={0};// save species info
      int species_num[2]={0};
      int num_diff[2]={0};   //save diffu events

      double prob_each[3][4]={
            //0    1    2    
            //diff  C    C2   e1 
      /*	{0.00,0.00,0.00,0.00},
            {0.20,1.00,0.00,0.00},//C 
            {0.00,0.00,0.00,2.30},//C2    e1:C2-> C+C
      */
          {0.00, 0.00, 0.00, 0.00},
          {0.50, 0.90, 0.00, 0.00},
          {0.49, 0.00, 0.00, 2.80},
      };
      // C2->C+C 2.7eV, C+C->C2 ???
      int sp_merge[2][2]={\
            //1	2
            //C	C2
            {2,0},//C
            {0,0},//C2
      };

      int sp_e[2][2]={\
            {0,0},  //C
            {1,1}};  //C2

      int evt_emerge[2][2]={\
            //1   2
            //C   C2
            {1,-1},//C
            {-1,-1},//C2
      };

      int evt_spec[2]={-1,2};

      int p[3][2];
      int q[3][2];

      void err(char* erro);
      void init();
      int get_nb(int x,int y,int xy,int i);
      void find_evt();
      void diffusion(int sp,int s_n,int evt);
      void merge(int sp1,int s_n,int evt);
      void spec_del(int sp,int s_n);
      void creat(int sp,int x,int y);
      void spec_e(int sp,int s_n,int evt);
      void update_evt_nb(int x,int y);
      void statistic(int n,int N);
      int get_sp(int s_x,int s_y);
      void add_c(int sp);

      class species{
      public:
            species(int sp,int x,int y){
                  spec=sp;
                  s_x=x;
                  s_y=y;
                  prob[3]=prob_each[spec][3];  //desorp or decomp events
                  check_event();
            }
            void check_event(){
                  double r9;
                  for(int i=0;i<3;i++){  //3 directions
                        nb[i][0]=get_nb(s_x,s_y,0,i);
                        nb[i][1]=get_nb(s_x,s_y,1,i);
                        event[i]=get_sp(nb[i][0],nb[i][1]);
                  //	if(event[i]==100) prob[i]=0; //2017 added for h
                  //	else prob[i]=prob_each[spec][event[i]];
                        prob[i]=prob_each[spec][event[i]];
                  }
                  prob_s=0;
                  for(int i=0;i<4;i++) prob_s+=prob[i];
            }
            int update(){
                  int i;
                  double evt_sum=0;
                  double evt_add=0;
                  double evt_rand;
                  for(i=0;i<4;i++)
                        if(prob[i]!=0) evt_sum+=prob[i];
                  evt_rand=evt_sum*(double)rand()/RAND_MAX;
                  for(i=0;i<4;i++){
                        if(prob[i]!=0) evt_add+=prob[i];
                        if(evt_add>=evt_rand){
                              return i;
                        }
                  }
                  err("spec.update()");
                  return 0;
            }

            double prob[4],prob_s;
            int event[3],nb[3][2];
            int spec,s_x,s_y;
      };

      vector<vector<species> > spec_list(2);

      int main(){
            init();
            int init_h=0,h;
            for(int i=0;i<2;i++) init_h+=species_num[i];
            for(int m=0;m<multiplier;m++){
                  for(int i=0;i<N_limit;i++){
            //		h=init_h;
                        find_evt();
            //		init_h=0;
            //		for(int j=0;j<2;j++) init_h+=species_num[j];
                        //if(init_h!=h) statistic(i,m);
                        if(i%step_out==0) statistic(i,0);
                  }
            }
            statistic(-1,0);
            for(int i=0;i<2;i++){
                  printf("num_evt %d:\t%d\n",i,num_evt[i]);
                  printf("num_diff %d:\t%d\n",i,num_diff[i]);
            }
            return 0;
      }

      void err(char* erro){
            printf("%s error!!!\n",erro);
            scanf("%s",&erro);
      }

      void init(){
            int i,j;
            srand((unsigned)time(NULL));
            for(i=1;i<3;i++)  //2 species
                  for(j=0;j<4;j++)   
                        if(prob_each[i][j]!=0)
                              prob_each[i][j]=2.71*pow(10,13)*exp(-prob_each[i][j]/kT);
            for(i=1;i<3;i++)
                  for(j=1;j<3;j++)
                        if(prob_each[i][j]!=0)
                              prob_each[i][j]=prob_each[i][j]/2;

            p[0][0]=-1;p[0][1]=1;// p for x even
            p[1][0]=-1;p[1][1]=0;
            p[2][0]=1;p[2][1]=0;
            q[0][0]=-1;q[0][1]=0;//q for x odd
            q[1][0]=1;q[1][1]=0;
            q[2][0]=1;q[2][1]=-1;

            for(i=0;i<c_num;i++) add_c(1);    

            //for(int i=row/2-G_row/2-1;i<row/2+G_row/2;i++)
            //for(int j=col/2-G_col/2-1;j<col/2+G_col/2;j++)
            //mesh[i][j][0]=9;
            //mesh[row/2-G_row/2-1][col/2-G_col/2-1][0]=100;
            //mesh[row/2-G_row/2-1][col/2+G_col/2][0]=100;
            //mesh[row/2+G_row/2][col/2-G_col/2-1][0]=100;
            //mesh[row/2+G_row/2][col/2+G_col/2][0]=100;
      }

      int get_nb(int x,int y,int xy,int i){
            int x_temp,y_temp;
            if(xy==0){
                  if(x%2==0)  x_temp=x+p[i][0];
                  else        x_temp=x+q[i][0];
                  if(x_temp>=row) return x_temp-=row;
                  else if(x_temp<0) return x_temp+=row;
                  else return x_temp;
            }
            else {
                  if(x%2==0)  y_temp=y+p[i][1];
                  else        y_temp=y+q[i][1];
                  if(y_temp>=col) return y_temp-=col;
                  else if(y_temp<0) return y_temp+=col;
                  else return y_temp;
            }
      }

      void find_evt(){
            double prob_rand;
            double prob_sum=0;
            double prob_add=0;
            int drct,s_n;
            double delta_t;
            for(int i=0;i<2;i++)
                  if(!spec_list[i].empty())
                        for(int j=0;j<spec_list[i].size();j++) prob_sum+=spec_list[i][j].prob_s;
            //printf("prob_s:\t%f\n",prob_sum);
            //
            do{
                  delta_t=(double)rand()/RAND_MAX;
            }while(delta_t==0);
            delta_t=-log(delta_t)/prob_sum;
            t+=delta_t;

            prob_rand=prob_sum*(double)rand()/RAND_MAX;
            for(int i=0;i<2;i++)
                  if(!spec_list[i].empty()){
                        for(int j=0;j<spec_list[i].size();j++){
                              prob_add+=spec_list[i][j].prob_s;
                              if(prob_add>=prob_rand){
                                    drct=spec_list[i][j].update();
                                    if(drct<3){
                                          if(spec_list[i][j].event[drct]==0){
                                                diffusion(i+1,j,drct);
                                                num_diff[i]++;
                                                //printf("diffuse cxhy");
                                                //
                                                //printf("get it1\n");
                                          }
                                          else if(spec_list[i][j].event[drct]<=2){
                                                merge(i+1,j,drct);
                                                //printf("get it2\n");
                                                //printf("merge cxhy\n");
                                          }
                                          else if(spec_list[i][j].event[drct]==100)
                                                return;
                                          else err("error in update1");
                                    }
                                    else  {
                                          spec_e(i+1,j,drct);
                                          if(evt_spec[i]!=-1) num_evt[evt_spec[i]-1]++;
                                    }
                                    return;
                              }
                        }
                  }
                  //err("prob");
      }

      void diffusion(int sp,int s_n,int drct){
            int x1,y1,x2,y2;
            x1=spec_list[sp-1][s_n].s_x;
            y1=spec_list[sp-1][s_n].s_y;
            x2=spec_list[sp-1][s_n].nb[drct][0];
            y2=spec_list[sp-1][s_n].nb[drct][1];
            if(mesh[x1][y1][0]!=sp||mesh[x2][y2][0]!=0){    //for debug
                  //printf("in diffu,sp,x1,y1,x2,y2:  %d\t%d\t%d\t%d\t%d\n",sp,x1,y1,x2,y2);
                  //if(mesh[x1][y1][0]!=sp) {printf("sp=%d,mesh=%d\n",sp,mesh[x1][y1][0]); err("diffusion1");}
                  if(mesh[x1][y1][0]!=sp)  printf("dif1");
                  if(mesh[x2][y2][0]!=0) printf("dif1");
                  printf("drct=%d\tsp1=%d,mesh[0]=%d\n",drct,sp,mesh[x1][y1][0]);
                  printf("event[drct]:%d",spec_list[sp-1][s_n].event[drct]);
                  printf("sp2=%d,mesh2[1]=%d\n",mesh[x2][y2][0],mesh[x2][y2][1]);
                  printf("x2=%d,y2[1]=%d\n",spec_list[sp-1][mesh[x2][y2][1]].s_x,spec_list[sp-1][mesh[x2][y2][1]].s_y);
                  for(int i=0;i<3;i++){
                        printf("evt[i]=%d\n",spec_list[sp-1][s_n].event[i]);
                        update_evt_nb(x2,y2);
                        printf("evt[i]=%d\n",spec_list[sp-1][s_n].event[i]);
                        spec_list[sp-1][s_n].check_event();
                        printf("evt[i]=%d\n",spec_list[sp-1][s_n].event[i]);
                        printf("neigbour of 1: %d\t%d\n",get_nb(x1,y1,0,i),get_nb(x1,y1,1,i));
                        printf("neigbour of 2: %d\t%d\n",get_nb(x2,y2,0,i),get_nb(x2,y2,1,i));
                  }
                  err("diffusion");
                  //}
                  err("diffusion");
            }
            mesh[x2][y2][0]=mesh[x1][y1][0];
            mesh[x2][y2][1]=mesh[x1][y1][1];
            mesh[x1][y1][0]=0;
            mesh[x1][y1][1]=0;
            spec_list[sp-1][s_n].s_x=x2;
            spec_list[sp-1][s_n].s_y=y2;
            spec_list[sp-1][s_n].check_event();
            update_evt_nb(x1,y1);
            update_evt_nb(x2,y2);
      }

      void merge(int sp1,int s_n,int drct){
            int sp2,sp_crt;
            int x1,y1,x2,y2;
            x1=spec_list[sp1-1][s_n].s_x;
            y1=spec_list[sp1-1][s_n].s_y;
            x2=spec_list[sp1-1][s_n].nb[drct][0];
            y2=spec_list[sp1-1][s_n].nb[drct][1];
            sp2=spec_list[sp1-1][s_n].event[drct];
            spec_del(sp1,s_n);
            spec_del(sp2,mesh[x2][y2][1]);
            sp_crt=sp_merge[sp1-1][sp2-1];
            if(evt_emerge[sp1-1][sp2-1]!=-1) num_evt[evt_emerge[sp1-1][sp2-1]-1]++;
            if(sp_crt>0) creat(sp_crt,x1,y1);
            else if(sp_crt==0) err("merge");
      }

      void spec_del(int sp,int s_n){
            int x,y;
            int spec_end;
            species_num[sp-1]--;
            x=spec_list[sp-1][s_n].s_x;
            y=spec_list[sp-1][s_n].s_y;
            if(sp!=mesh[x][y][0]) err("spec_del1");
            if(s_n!=mesh[x][y][1]) err("spec_del2");
            spec_end=spec_list[sp-1].size()-1;
            if(s_n!=spec_end){
                  //mesh[spec_list[sp-1][spec_end].s_x][spec_list[sp-1][spec_end].s_y][0]=sp;
                  mesh[spec_list[sp-1][spec_end].s_x][spec_list[sp-1][spec_end].s_y][1]=s_n;
                  swap(spec_list[sp-1][s_n],spec_list[sp-1][spec_end]);
            }
            spec_list[sp-1].pop_back();
            mesh[x][y][0]=0;
            mesh[x][y][1]=0;
            update_evt_nb(x,y);
      }

      void creat(int sp,int x,int y){
            species_num[sp-1]++;
            mesh[x][y][0]=sp;
            mesh[x][y][1]=spec_list[sp-1].size();
            spec_list[sp-1].push_back(species(sp,x,y));
            update_evt_nb(x,y);
      }
      void spec_e(int sp,int s_n,int drct){
            int sp1,sp2,xn,yn;
            int x,y;
            x=spec_list[sp-1][s_n].s_x;
            y=spec_list[sp-1][s_n].s_y;
            sp1=sp_e[sp-1][0];
            sp2=sp_e[sp-1][1];
            // revised 0925
            if(sp1==0)    err("spec_e");
            spec_del(sp,s_n);

            creat(sp1,x,y);

            for(int i=0;i<3;i++){
                  xn=get_nb(x,y,0,i);
                  yn=get_nb(x,y,1,i);
                  if(mesh[xn][yn][0]==0){
                        creat(sp2,xn,yn);
                        break;
                  }
            }
      }

      void update_evt_nb(int x,int y){
            int sp,s_n;
            int x_temp,y_temp;
            for(int i=0;i<3;i++){
                  x_temp=get_nb(x,y,0,i);
                  y_temp=get_nb(x,y,1,i);
                  sp=mesh[x_temp][y_temp][0];
                  if(sp>0&&sp<=8){
                        s_n=mesh[x_temp][y_temp][1];
                        spec_list[sp-1][s_n].check_event();
                  }
            }
      }

      void statistic(int n,int N){
            int nn[2];
            for(int i=0;i<2;i++) nn[i]=spec_list[i].size();
            printf("time/c/c2:\t%e\t%d\t%d\n",t,species_num[0],species_num[1]);
      }

      int get_sp(int x,int y){
            return mesh[x][y][0];
      }

      void add_c(int sp){
            int x,y,xn,yn;
            int flag=0;
            do{
                  do{
                        x=(int)(row*(double)rand()/RAND_MAX);
                        y=(int)(col*(double)rand()/RAND_MAX);
                  }while(mesh[x][y][0]!=0);
                  for(int i=0;i<3;i++){    
                        xn=get_nb(x,y,0,i);
                        yn=get_nb(x,y,1,i);
                        if(mesh[xn][yn][0]==0){
                              flag=1;
                              break;
                        }
                  }
            }while(flag==0);
            creat(sp,x,y);
      }

