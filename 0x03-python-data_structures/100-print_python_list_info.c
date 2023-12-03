#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    const char *type;

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        type = Py_TYPE(PyList_GetItem(p, i))->tp_name;
        printf("Element %ld: %s\n", i, type);
    }
}