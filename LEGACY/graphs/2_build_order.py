"""

CTCI - TREES AND GRAPHS: QUESTION 7

You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second
project is dependent on the first project). All of a project's dependencies must be built before the project is. Find
a build order that will allow the projects to be built. If there is no valid build order, raise an error.

(Topological sort problem)

EXAMPLE:
    INPUT: Projects: a, b, c, d, e, f
           Dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

    OUTPUT: f, e, a, b, d, c

"""


def find_build_order(project_names, dependencies):
    """
    :param project_names: list of strings
    :param dependencies: list of pair of strings
    :return: list of projects
    """

    graph = build_graph(project_names, dependencies)
    return order_projects(graph.nodes())


def build_graph(project_names, dependencies):
    graph = TopologicalGraph()

    for project_name in project_names:
        graph.get_or_create_node(project_name)

    for dependency_pair in dependencies:
        first, second = dependency_pair[0], dependency_pair[1]
        graph.add_edge_between(first, second)  # Second has a dependency to first

    return graph


def order_projects(projects):
    order = [None] * len(projects)

    # First, we add the projects without dependencies.
    end_of_list_index = add_non_dependent_projects(projects, order, 0)

    to_be_processed = 0
    while to_be_processed < len(order):
        current_project = order[to_be_processed]
        if not current_project: raise ValueError("Graph has a circular dependency. No build order is possible.")
        children = current_project.children()
        for child in children:
            child.remove_dependency()  # Remove dependency between current_project and it's children
        # Add children projects that have no dependencies
        end_of_list_index = add_non_dependent_projects(children, order, end_of_list_index)
        to_be_processed += 1
    return order


def add_non_dependent_projects(projects, order, starting_index):
    starting_index = starting_index
    for project in projects:
        if project.amount_of_dependencies() == 0:
            order[starting_index] = project
            starting_index += 1
    return starting_index


class Project(object):  # It's a graph node that also has a dependency count and a map.
    def __init__(self, name):
        self._amount_of_dependencies = 0
        self._name = name
        self._children = []
        self._children_map = {}  # Maps a project name to it's project node, to find it faster

    def __str__(self):
        return str(self.name())

    def children(self):
        return self._children

    def name(self):
        return self._name

    def amount_of_dependencies(self):
        return self._amount_of_dependencies

    def add_dependency(self):
        self._amount_of_dependencies += 1

    def remove_dependency(self):
        self._amount_of_dependencies -= 1

    def add_neighbor(self, project):  # The project passed by parameter will have a dependency to self.
        if not(project.name() in self._children_map):
            self.children().append(project)
            self._children_map.update({project.name(): project})
            project.add_dependency()


class TopologicalGraph(object):
    def __init__(self):
        self._nodes = []
        self._node_map = {}  # Maps a project name to it's project node, to find it faster.

    def nodes(self):
        return self._nodes

    def get_or_create_node(self, name):
        if not (name in self._node_map):
            project = Project(name=name)
            self.nodes().append(project)
            self._node_map.update({name: project})
        return self._node_map[name]

    def create_node(self, project):
        if not (project.name() in self._node_map):
            self._node_map.update({project.name(): project})
            self.nodes().append(project)

    def add_edge_between(self, start_name, end_name):  # End name will have a dependency to start name
        project_start = self.get_or_create_node(start_name)
        project_end = self.get_or_create_node(end_name)
        project_start.add_neighbor(project_end)