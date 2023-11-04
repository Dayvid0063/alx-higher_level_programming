#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Func prints info on PY
 * @p: Python
 */
void print_python_list_info(PyObject *p)
{
	int u;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (u = 0; u < Py_SIZE(p); u++)
		printf("Element %d: %s\n", u, Py_TYPE(PyList_GetItem(p, u))->tp_name);
}
