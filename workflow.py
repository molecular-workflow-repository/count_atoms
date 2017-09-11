import molflow.definitions as mf

wf = mf.WorkflowDefinition("count_atoms")
__workflow__ = wf

# Functions
counter = mf.Function(sourcefile='./functions.py', funcname='count')

# Inputs
mol = wf.add_input('molecule', type='mdt', description='Molecule to count the atoms of.')

# DAG
numatoms = counter(mol)

# Outputs
wf.set_output(numatoms, 'numatoms', type='int')
