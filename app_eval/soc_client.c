#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <time.h>

int
main()
{
  struct sockaddr_in server;
  int sock;
  int n;

  int buf_size =1024;
  char buf[buf_size];
  char rx_buf[buf_size];
  char * keyword = "measurement";
  char excess[1010] = {'\0'};

  clock_t start,end;

  sock = socket(AF_INET, SOCK_STREAM, 0);

  server.sin_family = AF_INET;
  server.sin_port = htons(8080);
  server.sin_addr.s_addr = inet_addr("10.10.0.11");

  connect(sock, (struct sockaddr *)&server, sizeof(server));

  start = clock();
  for ( int i = 0; i < 1000; i++ ){
    //printf( "[CLIENT]       :%d\n", i );
    sprintf(buf, "%d, %s, %s", i, keyword, excess);
    if( send( sock, buf, buf_size, 0 ) < 0 ) {
      perror( "send" );
    } else {
      recv( sock, rx_buf, buf_size, 0 );
    }
    printf( "counter :    %d\n", i );
  }
  end = clock();
  printf("%f秒かかりました\n",(double)(end-start)/CLOCKS_PER_SEC);

  ///* サーバからデータを受信 */
  //memset(buf, 0, sizeof(buf));
  //n = read(sock, buf, sizeof(buf));

  //printf("%d, %s\n", n, buf);

  /* socketの終了 */
  close(sock);
  return 0;
}
