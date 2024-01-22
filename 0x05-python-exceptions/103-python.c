#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;

    if (!PyList_Check(p))
    {
        printf("[*] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(item))
        {
            printf("bytes\n");
            print_python_bytes(item);
        }
        else if (PyFloat_Check(item))
        {
            printf("float\n");
            print_python_float(item);
        }
        else if (PyTuple_Check(item) || PyList_Check(item))
        {
            printf("tuple\n");
            print_python_list(item);
        }
        else if (PyLong_Check(item))
        {
            printf("int\n");
            printf("[.] int object info\n");
            printf("  value: %ld\n", PyLong_AsLong(item));
        }
        else if (PyUnicode_Check(item))
        {
            printf("str\n");
        }
        else
        {
            printf("unknown\n");
        }
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    PyBytesObject *bytes;

    if (!PyBytes_Check(p))
    {
        printf("[.] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);

    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes: ", (size + 1 > 10) ? 10 : size + 1);
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x ", bytes->ob_sval[i] & 0xff);
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    double value;

    if (!PyFloat_Check(p))
    {
        printf("[.] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);

    printf("[.] float object info\n");
    printf("  value: %.17g\n", value);
}
