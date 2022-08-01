#version 120

varying vec2 fTexcoords;
uniform sampler2D textureObj;

void main()
{
    gl_FragColor = texture2D(textureObj, fTexcoords);
}
