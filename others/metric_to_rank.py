# datasets_1 <- c("Avianuce", "Cetacean", "Lepidoptera", "Papilionidae", "Pseudapis", "Seedplant", "Shenanimal", "Shenfungi", "Shenplant", "Songmammals", "UCEminus105", "1KP", "Fengfrog")

datasets_1 = {
    "Avianuce":1,
    "Cetacean":2,
    "Lepidoptera":3,
    "Papilionidae":4,
    "Pseudapis":5,
    "Seedplant":6,
    "Shenanimal":7,
    "Shenfungi":8,
    "Shenplant":9,
    "Songmammals":10,
    "UCEminus105":11,
    "1KP":12,
    "Fengfrog":13
}

# datasets_caster <- c("Anoplura", "Batrachoseps", "Fumaria", "Lampropeltis", "Oryza")
index_bias = 13
datasets_2 = {
    "Anoplura":1,
    "Batrachoseps":2,
    "Fumaria":3,
    "Lampropeltis":4,
    "Oryza":5
}

# Metrics dictionary, where type is 0 for balance and 1 for imbalance
metrics = {
    "b1": {'index':1, 'type':0},
    "b2": {'index':2, 'type':0},
    "max_width": {'index':3, 'type':0},
    "rooted_quartet": {'index':4, 'type':0},
    "avg_leaf_depth": {'index':5, 'type':1},
    "avg_vertex_depth": {'index':6, 'type':1},
    "colless": {'index':7, 'type':1},
    "max_depth": {'index':8, 'type':1},
    "sackin": {'index':9, 'type':1},
    "stairs1": {'index':10, 'type':1},
    "stairs2": {'index':11, 'type':1},
    "symmetry_nodes": {'index':12, 'type':1},
    "total_cophenetic": {'index':13, 'type':1}
}

methods_1 = ['ASTRAL-III', 'ASTER', 'ASTRID', 'TreeQMC']
methods_2 = ['CASTER-pair', 'CASTER-site']

# For all methods in methods_1, and datasets in datasets_1, the metric data is located in ../metrics/{dataset}/{method}.json
# You need to compare the metrics of different methods for each dataset, and then rank the methods for each dataset. 
# For metrics with type 0, you need to sort the metrics in ascending order.
# For metrics with type 1, you need to sort the metrics in descending order.
# You need to output the rank of each method for each dataset.

# write a function to check a dataset first:
import json
import os

def get_color_mapping(ranks):
    """
    Determine colors based on ranking pattern
    ranks: list of ranks for a specific metric and dataset
    returns: dictionary mapping ranks to colors
    """
    if not ranks:  # Handle empty ranks case
        return {}
        
    unique_ranks = sorted(list(set(ranks)))
    n_unique = len(unique_ranks)
    
    if n_unique == 1:
        # All ranks are the same (1111)
        return {rank: 'rdbu4' for rank in unique_ranks}
    
    if n_unique == 2:
        # Pattern like 1144
        return {
            unique_ranks[0]: 'rdbu1',
            unique_ranks[1]: 'rdbu7'
        }
    
    if n_unique == 3:
        # Patterns like 1224 or 1233
        rank_counts = {rank: ranks.count(rank) for rank in unique_ranks}
        if max(rank_counts.values()) == 2:
            if rank_counts[unique_ranks[1]] == 2:
                # Pattern 1224
                return {
                    unique_ranks[0]: 'rdbu1',
                    unique_ranks[1]: 'rdbu4',
                    unique_ranks[2]: 'rdbu7'
                }
            else:
                # Pattern 1233
                return {
                    unique_ranks[0]: 'rdbu1',
                    unique_ranks[1]: 'rdbu3',
                    unique_ranks[2]: 'rdbu6'
                }
        else:
            # Three unique ranks but not 1224 or 1233
            return {
                unique_ranks[0]: 'rdbu1',
                unique_ranks[1]: 'rdbu4',
                unique_ranks[2]: 'rdbu7'
            }
    
    if n_unique == 4:
        # Pattern 1234
        return {
            unique_ranks[0]: 'rdbu1',
            unique_ranks[1]: 'rdbu3',
            unique_ranks[2]: 'rdbu5',
            unique_ranks[3]: 'rdbu7'
        }
    
    # Default case - should not happen with 4 methods
    return {rank: 'rdbu4' for rank in unique_ranks}

def check_dataset(dataset_name, dataset_index):
    # Dictionary to store metrics for each method
    method_metrics = {}
    
    # Read metrics for each method
    for method in methods_1:
        file_path = f"../metrics/{dataset_name}/{method}.json"
        try:
            with open(file_path, 'r') as f:
                method_metrics[method] = json.load(f)
        except FileNotFoundError:
            print(f"Warning: File not found - {file_path}")
            continue
    
    # If no methods were found, return empty rankings
    if not method_metrics:
        return {}

    # Dictionary to store rankings and colors
    rankings = {}
    
    # For each metric, rank the methods
    for metric_name, metric_info in metrics.items():
        metric_type = metric_info['type']
        metric_index = metric_info['index']
        
        # Get metric values for methods that have data
        metric_values = []
        for method, metrics_data in method_metrics.items():
            if metric_name in metrics_data:
                metric_values.append((method, metrics_data[metric_name][0]))
        
        if not metric_values:  # Skip if no data for this metric
            continue
            
        # Sort based on metric type (0: ascending, 1: descending)
        sorted_methods = sorted(metric_values, 
                              key=lambda x: x[1], 
                              reverse=(metric_type == 1))
        
        # Get ranks for all methods
        current_rank = 1
        prev_value = None
        ranks = []
        rank_mapping = {}
        
        for i, (method, value) in enumerate(sorted_methods):
            if prev_value is not None and value != prev_value:
                current_rank = i + 1
            rank_mapping[method] = current_rank
            ranks.append(current_rank)
            prev_value = value
        
        # Get color mapping based on ranks
        color_mapping = get_color_mapping(ranks)
        
        # Assign ranks and colors
        rank_key = f"{dataset_index}-{metric_index}"
        for method, rank in rank_mapping.items():
            if method not in rankings:
                rankings[method] = {}
            rankings[method][rank_key] = {
                'rank': rank,
                'color': color_mapping[rank]
            }
            
    return rankings

def check_all_datasets():
    results = {method: {} for method in methods_1}
    
    # Iterate through datasets using the dictionary
    for dataset_name, dataset_index in datasets_1.items():
        dataset_rankings = check_dataset(dataset_name, dataset_index)
        
        # Merge rankings into results
        for method in methods_1:
            if method in dataset_rankings:
                results[method].update(dataset_rankings[method])
    
    return results


# color_mapping

results = check_all_datasets()
# Save results to a JSON file
output_file = "rankings.json"
with open(output_file, 'w') as f:
    json.dump(results, f, indent=2)
print(f"Rankings saved to {output_file}")
