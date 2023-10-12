class OutOfBoundsException(Exception):
    pass


class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """

    def __init__(self, value, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        """
        self._value = value
        self._next = next

    @property
    def value(self):
        """
        Retorna o valor do nó atual
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário
        """
        return self._next is not None


class LinkedList(object):
    def __init__(self):
        """
        Construtor de lista ligada. A lista sempre começa vazia
        """
        self._head = None  # Apontador para o nó cabeça (primeiro)
        self._tail = None  # Apontador para o nó filho (ultimo)
        self._len = 0  # contador

    def __len__(self):
        return self._len

    @property
    def head(self):
        """
        Esta propriedade deve retornar o valor do primeiro nó da lista ligada
        """
        if not self._head:
            return None
        return self._head.value

    @property
    def tail(self):
        """
        Esta propriedade deve retornar o valor do último nó da lista ligada
        """
        if not self._tail:
            return None
        return self._tail.value

    def append(self, value):
        """
        Esta função deve inserir um novo nó no FINAL da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - append(0) - [1, 2, 3, 0]
        """
        linked_list_node = LinkedListNode(value)
        current = self._head
        if current:
            while current.next:
                current = current.next
            current.next = linked_list_node
            self._tail = linked_list_node
        else:
            self._head = linked_list_node
            self._tail = linked_list_node
        self._len += 1

    def insert(self, value):
        """
        Esta função deve inserir um novo nó no INICIO da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - insert(0) - [0, 1, 2, 3]
        """
        linked_list_node = LinkedListNode(value)
        linked_list_node.next = self._head
        self._head = linked_list_node
        self._len += 1


    def removeFirst(self):
        """
        Esta função deve remover o primeiro elemento da lista e retornar o seu valor.
        Apos a execução, a lista ligada deve ter um elemento a menos.
        """
        if not self._head:
            return None
        temp = self._head
        value = temp.value
        self._head = self._head.next
        temp = None
        self._len -= 1
        return value

    def getValueAt(self, index):
        """
        Esta função deve retornar o valor de um nó na posição definida por INDEX.
        Se o index for maior do que o tamanho da lista, retornar OutOfBoundsException
        """
        if index > self._len:
            raise OutOfBoundsException('index greather than len')

        count = 0
        current = self._head

        if current:
            while count != index:
                current = current.next
                count += 1
            if current:
                return current.value
        return None

    def toList(self):
        """
        Esta função retornar uma representação em forma de vetor ([1, 2, 3....])
        da lista ligada
        """
        items = []
        current = self._head
        
        while current != None:
            items.append(current.value)
            current = current.next
        return items