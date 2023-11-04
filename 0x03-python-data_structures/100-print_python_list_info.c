#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Func prints info on PY
 * @p: Python
 */
void print_python_list_info(PyObject *p)
{
	int len, fix, u;
	PyObject *obj;

	len = Py_SIZE(p);
	fix = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", fix);

	for (u = 0; u < size; u++)
	{
		printf("Element %d: ", u);

		obj = PyList_GetItem(p, u);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
