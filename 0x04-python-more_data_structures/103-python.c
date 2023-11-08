#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about a Python list
 * @p: Pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: Pointer to a PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		size = Py_SIZE(p);
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", PyBytes_AsString(p));

		printf("  first %d bytes: ", (int)size > 10 ? 10 : (int)size);
		for (i = 0; i < (size > 10 ? 10 : size); i++)
		{
			printf("%02x", bytes->ob_sval[i] & 0xff);
			if (i < ((size > 10) ? 10 : size) - 1)
				printf(" ");
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
