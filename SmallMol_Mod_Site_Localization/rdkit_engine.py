from rdkit.Chem import *
from rdkit import Chem, Geometry
from rdkit.Chem import AllChem, Descriptors
from . import pars
bondtype2string = {v:k for (k, v,) in Chem.rdchem.BondType.names.items()}

class newclass(object):
    """
    Additional class
    """

    pass

def LogP(mol):
    return Chem.Crippen.MolLogP(mol)



def natoms(mol):
    return mol.GetNumAtoms()



def GetExtendedAtomMass(mol, a):
    atom = mol.GetAtomWithIdx(a)
    return pars.mims[atom.GetSymbol()] + pars.Hmass * (atom.GetNumImplicitHs() + atom.GetNumExplicitHs())



def GetAtomSymbol(mol, a):
    return mol.GetAtomWithIdx(a).GetSymbol()



def GetAtomHs(mol, a):
    atom = mol.GetAtomWithIdx(a)
    return atom.GetNumImplicitHs() + atom.GetNumExplicitHs()



def nbonds(mol):
    return mol.GetNumBonds()



def GetBondAtoms(mol, b):
    bond = mol.GetBondWithIdx(b)
    return [bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()]



def GetNBonds(mol, a):
    return len(mol.GetAtomWithIdx(a).GetBonds())



def GetBondType(mol, b):
    bond = mol.GetBondWithIdx(b)
    return bondtype2string[bond.GetBondType()]



def MolToInchiKey(mol):
    return AllChem.InchiToInchiKey(AllChem.MolToInchi(mol))



def FragmentToInchiKey(mol, atomlist):
    emol = Chem.EditableMol(mol)
    for atom in reversed(range(mol.GetNumAtoms())):
        if atom not in atomlist:
            emol.RemoveAtom(atom)

    frag = emol.GetMol()
    return Chem.MolToSmiles(frag)



def GetFormulaProps(mol):
    mim = 0.0
    for a in range(mol.GetNumAtoms()):
        mim += GetExtendedAtomMass(mol, a)

    formula_string = Chem.rdMolDescriptors.CalcMolFormula(mol)
    return (mim, formula_string)



def SmilesToMol(smiles, name = None):
    mol = Chem.MolFromSmiles(smiles)
    mol.SetProp('_Name', name)
    AllChem.Compute2DCoords(mol)
    return mol
