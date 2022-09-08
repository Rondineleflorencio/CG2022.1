#include <stdio.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include <stdlib.h>

void inicio(void);
void desenha(void);


int main(int argc, char** argv){
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_DEPTH | GLUT_SINGLE | GLUT_RGBA);
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(640, 480);
    glutCreateWindow(",sjsngsnkç");
    
    inicio();
    
    glutDisplayFunc(desenha);
    glutMainLoop();
    return 0;
}

void inicio()
{
	glClearColor(0,0,0,0);
}

void desenha(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glBegin(GL_TRIANGLES);
	glVertex2f(-0.5,-0.5);
	glColor3f(1,0,0);
	glVertex2f(0.5,-0.5);
	glColor3f(1,0,0);
	glVertex2f(0.5,0.5);
	glColor3f(1,0,0);
	glEnd();
	glFlush();
}



