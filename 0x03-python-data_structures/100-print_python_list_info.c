#include <Python.h>

/**
 * print_python_list_info - Func prints info on PY list
 * @p: Obj P
 */
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p);
	int u;
	PyObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (u = 0; u < size; u++)
		printf("Element %d: %s\n", u, Py_TYPE(obj->PyList_GetItem(p, u))->tp_name);
}
