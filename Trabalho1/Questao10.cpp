#include <stdio.h>
#include <stdlib.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
void renderiza()
{
 glClearColor( 0.2, 0.2, 0.2, 3 );
 glClear( GL_COLOR_BUFFER_BIT );
 glBegin(GL_QUADS);
	 glColor3f(0.4,0.4,1);
	 glVertex2f(-1,1);
	 glColor3f(1,0,0);
	 glVertex2f(-1,-1);
	 glColor3f(1,0,0);
	 glVertex2f(1,-1);
	 glColor3f(0.4,0.4,1);
	 glVertex2f(1,1);
 glEnd();
 
  glBegin(GL_QUADS);
	 glColor3f(0.5,0.8,0.3);
	 glVertex2f(-1,-0.5);
	 glColor3f(0,0.6,0);
	 glVertex2f(-1,-1);
	 glColor3f(0,0.6,0);
	 glVertex2f(1,-1);
	 glColor3f(0.5,0.8,0.3);
	 glVertex2f(1,-0.5);
 glEnd();
 	//triangulos
 glBegin( GL_TRIANGLES );
	 glColor3f( 1, 0.4, 0 );
	 glVertex2f( -0.9, -0.3 );
	 glColor3f( 1, 1, 0 );
	 glVertex2f( -0.3, -0.3 );
	 glColor3f( 1, 1, 0 );
	 glVertex2f( -0.6, 0.2 );
 glEnd();
 glBegin( GL_TRIANGLES );
	 glColor3f( 1, 1, 0 );
	 glVertex2f( -0.3, -0.3 );
	 glColor3f( 1, 0.4, 0 );
	 glVertex2f( 0.3, -0.3 );
	 glColor3f( 1, 1, 0 );
	 glVertex2f( 0, 0.2 );
 glEnd();
 glBegin( GL_TRIANGLES );
	 glColor3f( 1, 1, 0 );
	 glVertex2f( -0.6, 0.2 );
	 glColor3f( 1, 1, 0 );
	 glVertex2f( 0, 0.2 );
	 glColor3f( 1, 0.4, 0 );
	 glVertex2f( -0.3, 0.7);
 glEnd();
 glutSwapBuffers();
}
int main(int argc, char ** argv)
{
 glutInit( &argc, argv );
 glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB );
 glutInitWindowSize( 400, 400 );
 glutCreateWindow( "Trabalho 1" );
 glutDisplayFunc( renderiza );
 glutMainLoop();

 return 0;
}
