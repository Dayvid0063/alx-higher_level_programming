#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Func prints PY bytes
 * @p: PY object
 */
void print_python_bytes(PyObject *p)
{
	int u;
	long int size;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str, &size);
	printf("  size: %li\n", size);
	printf("  string: %s\n", str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (u = 0; u <= size && u < 10; u++)
		printf(" %02hhx", str[u]);
	printf("\n");
}

/**
 * void print_python_list - Func prints PY list
 * @p: PY object
 */
void print_python_list(PyObject *p)
{
	int u;
	long int size = PyList_Size(p);
	allocate = list->allocated;
	PyListObject *list = (PyListObject *)p;
	const char *data;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", allocate);
	for (u = 0; u < size; u++)
	{
		data = (list->ob_item[u])->ob_type->tp_name;
		printf("Element %i: %s\n", u, data);
		if (!strcmp(data, "bytes"))
			print_python_bytes(list->ob_item[u]);
	}
}
