# Proyecto: Traductor de GCL a su Semántica

GCL (Guarded Command Language) es un lenguaje de programación imperativo que usa el comando de
múltiples guardias, para la instrucción de selección e iteración, soporta tipo de datos entero, booleanos
y arreglos de enteros. Se han omitido características normales de otros lenguajes, tales como llamadas
a procedimientos y funciones, tipos de datos compuestos y números punto flotante, con el objetivo de
simplificar su dise ̃no y hacer factible la elaboración de un interpretador a lo largo de un trimestre.

## Etapa 1: Analisis lexicográfico

Compilar con:
```
./run.sh ../CasosDePrueba/Tests/<Prueba>.gcl
```
Fuentess:

- [PLY (Python Lex-Yacc) - Documentación](https://www.dabeaz.com/ply/ply.html)
- [Lenguaje de RegEx en python](https://docs.python.org/es/3/library/re.html)
- [Lenguaje de RegEx - Referencia rápida](https://learn.microsoft.com/es-es/dotnet/standard/base-types/regular-expression-language-quick-reference)
- [Analizador Lexico en python - Youtube](https://www.youtube.com/watch?v=gWrmCOTrtrs)

## Etapa 2: Analisisa Sintático con Árbol Sintáctico Abstracto (AST)
