#include <Python.h>

/**
 * print_python_bytes - Func prints PY bytes
 * @p: PY object
 */
void print_python_bytes(PyObject *p)
{
	int size, u;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &str, &size);
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (u = 0; u <= size && u < 10; u++)
		printf(" %02hhx", str[u]);
	printf("\n");
}

/**
 * print_python_list - Func prints PY list
 * @p: PY object
 */
void print_python_list(PyObject *p)
{
	int u, size, allocate;
	PyListObject *list = (PyListObject *)p;
	const char *obj;

	size = PyList_Size(p);
	allocate = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", allocate);
	for (u = 0; u < size; u++)
	{
		obj = (list->ob_item[u])->ob_type->tp_name;
		printf("Element %i: %s\n", u, obj);
		if (!strcmp(obj, "bytes"))
			print_python_bytes(list->ob_item[u]);
	}
}
