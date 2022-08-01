from OpenGL.GL import *
from OpenGL.GL.shaders import *
from pygame.locals import *
import pygame

width, height = 800, 600
REAL_RES = (800, 600)
VIRTUAL_RES = (width, height)

pygame.init()
pygame.display.set_mode(REAL_RES, OPENGL | DOUBLEBUF)

class Shader:
    def __init__(self, screen):
        self.screen = screen
        glViewport(0, 0, width, height)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        shaderObj = self.create("shaders/vertex.glsl", "shaders/fragment.glsl")
        vertices, texcoords, vertexShader, fragmentShader = shaderObj
        
        self.picture_exchange()
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        shaderProgram = glCreateProgram()
        glAttachShader(shaderProgram, vertexShader)
        glAttachShader(shaderProgram, fragmentShader)
        glLinkProgram(shaderProgram)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, vertices)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, texcoords)
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)

        glUseProgram(shaderProgram)
        glUniform1i(glGetUniformLocation(shaderProgram, "textureObj"), 0)

    def picture_exchange(self):
        self.textureData = pygame.image.tostring(self.screen, "RGB", True)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, self.textureData)

    def getFileContent(self, file):
        with open(file, 'r') as file:
            content = file.read()
        return content

    def create(self, vertexShaderPath, fragmentShaderPath):
        global timeMessage
        texcoords = [0, 0,  
                    0, 1, 
                    1, 1,  
                    1, 0]
        vertices = [-1, -1,  
                    -1, 1, 
                    1, 1,  
                    1, -1]
        vertexShader = compileShader(self.getFileContent((vertexShaderPath)), GL_VERTEX_SHADER)
        fragmentShader = compileShader(self.getFileContent((fragmentShaderPath)), GL_FRAGMENT_SHADER)
        shader = (vertices, texcoords, vertexShader, fragmentShader)
        return shader

    def render(self):
        self.picture_exchange()
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_QUADS, 0, 4)
        # data = glReadPixels(0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE)。
        pygame.display.flip()

    def __call__(self):
        return self.render()