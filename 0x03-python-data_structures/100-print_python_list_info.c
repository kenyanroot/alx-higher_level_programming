#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: PyObject pointer to a Python list.
 *
 * Description: This function prints the size of the Python list,
 * the allocated space, and the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;
    const char *type_name;
    PyListObject *list;

    list = (PyListObject *)p;
    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        type_name = item->ob_type->tp_name;
        printf("Element %zd: %s\n", i, type_name);
    }
}
