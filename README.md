
# DNA Sequence Alignment and Protein Structure Prediction

## Project Overview

This project performs `DNA sequence alignment` and `protein secondary structure prediction`. Global and local alignment algorithms are implemented. `Chou-Fasman algorithm` has been implemented for predicting protein secondary structures based on amino acid sequences.

## Features

- **Global Sequence Alignment:** Aligns two DNA sequences using the Needleman-Wunsch algorithm.
- **Local Sequence Alignment:** Aligns regions of similarity within two DNA sequences using the Smith-Waterman algorithm.
- **Protein Structure Prediction:** Predicts secondary structures (alpha helices, beta sheets, and turns) using the Chou-Fasman algorithm.

## Installation

To get started, clone the repository and ensure you have Python installed:

\`\`\`bash
git clone `https://github.com/your-repo/DNA-Sequence-Alignment-and-Protein-Structure-Prediction.git`
cd DNA-Sequence-Alignment-and-Protein-Structure-Prediction
\`\`\`

Install any necessary Python packages:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

_Note: The \`requirements.txt\` file should be added with the necessary dependencies._

## Usage

### Global Sequence Alignment

To perform a global sequence alignment, run the following command:

'bash
python GlobalAlignment.py sequence1.txt sequence2.txt
'

### Local Sequence Alignment

To perform a local sequence alignment, use:

'bash
python LocalAlignment.py sequence1.txt sequence2.txt
'

### Protein Secondary Structure Prediction

To predict the secondary structure of a protein sequence:

\`\`\`bash
python ChouFasman.py protein_sequence.txt
\`\`\`

The output will be saved in `secondary_structure_output.txt`.

## Output

The `secondary_structure_output.txt` file will contain the predicted secondary structure for the input protein sequence, indicating regions of alpha helices, beta sheets, and turns.


