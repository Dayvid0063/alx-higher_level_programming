#include <Python.h>

/**
 * print_python_bytes - Func prints PY bytes
 * @p: PY object
 */
void print_python_bytes(PyObject *p)
{
	long int u, v, size;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size > 10)
		v = 10;
	else
		v = size + 1;
	printf("  first %ld bytes:", v);
	for (u = 0; u < v; u++)
		if (str[u] > 0)
			printf(" %02x", str[u]);
		else
			printf(" %02x", 256 + str[u]);
	printf("\n");
}

/**
 * print_python_list - Func prints PY list
 * @p: PY object
 */
void print_python_list(PyObject *p)
{
	long int u, size;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (u = 0; u < size; u++)
	{
		obj = ((PyListObject *)p)->ob_item[u];
		printf("Element %ld: %s\n", u, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
