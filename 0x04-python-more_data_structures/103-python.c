#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;
    PyObject *repr;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);
    repr = PyObject_Repr(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x", str[i] & 0xFF);
        if (i < 9)
            printf(" ");
    }
    printf("\n");
    Py_XDECREF(repr);
}
