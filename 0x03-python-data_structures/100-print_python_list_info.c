#include <Python.h>

/**
 * print_python_list_info - Func prints info on PY
 * @p: Python
 */
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p);
	int alloc = ((PyListObject *)p)->allocated;
	int u;
	PyObject *obj;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (u = 0; u < size; u++)
	{
		printf("Element %d: ", u);

		obj = PyList_GetItem(p, u);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
