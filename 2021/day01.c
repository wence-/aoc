#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

int main(void) {
  int p1 = 0;
  int p2 = 0;
  int v1, v2, v3, v, i;
  int fd = open("../inputs/2021/day01.input", O_RDONLY);
  char *f;
  struct stat s;
  fstat(fd, &s);
  f = mmap(0, s.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
  v1 = INT32_MAX;
  v2 = INT32_MAX;
  v3 = INT32_MAX;
  v = 0;
  i = 0;
  while (i < s.st_size) {
    char c = f[i++];
    switch (c) {
    case '\n':
      p1 += (v1 < v);
      p2 += (v3 < v);
      v3 = v2;
      v2 = v1;
      v1 = v;
      v = 0;
      break;
    case '0':
    case '1':
    case '2':
    case '3':
    case '4':
    case '5':
    case '6':
    case '7':
    case '8':
    case '9':
      v = v * 10 + (c - '0');
      break;
    default:
      abort();
    }
  }
  munmap((void *)f, s.st_size);
  close(fd);
  printf("%d\n", p1);
  printf("%d\n", p2);
  return 0;
}
