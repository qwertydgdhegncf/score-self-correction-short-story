"""Check reported aggregate numbers. This does not run or retrain an LLM."""
from pathlib import Path
import csv,json,math
ROOT=Path(__file__).resolve().parents[1]
def verify(name):
    rows=list(csv.DictReader((ROOT/f'data/{name}.csv').open()))
    for r in rows:
        delta=float(r['delta_percentage_points'])
        assert math.isclose(float(r['accuracy_t2_percent'])-float(r['accuracy_t1_percent']),delta,abs_tol=0.11),r
        if 'recovery_share_percent' in r:
            assert math.isclose(float(r['recovery_share_percent'])-float(r['damage_share_percent']),delta,abs_tol=0.11),r
    return len(rows)
counts={name:verify(name) for name in ['math_results','humaneval_results','ablation_results']}
result={
    'analysis_type':'Arithmetic verification of published tables, not a model replication',
    'source':'https://arxiv.org/html/2409.12917v2',
    'rows_verified':counts,
    'math500_score':{
        'n':500,'initial_correct':300,'initial_wrong':200,
        'repaired':29,'damaged':7,'final_correct':322,
        'net_gain_percentage_points':(29-7)/500*100,
        'conditional_repair_percent':29/200*100,
        'conditional_damage_percent':7/300*100,
        'improvement_in_delta_vs_base_percentage_points':4.4-(-11.2),
        'final_accuracy_gain_vs_base_percentage_points':64.4-41.4,
    },
    'humaneval_rounding_note':'Printed one-decimal accuracies and deltas can differ by 0.1 pp after subtraction; values remain as reported.',
}
print(json.dumps(result,indent=2))
