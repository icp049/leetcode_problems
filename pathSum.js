varhasPathSum(root, targetSum) {
  if (!root) {
    // If the tree is empty, no path can sum up to the targetSum.
    return false;
  }

  // Check if the current node is a leaf node and if its value is equal to the remaining targetSum.
  if (!root.left && !root.right && root.val === targetSum) {
    return true;
  }

  // Recursively check the left and right subtrees with the reduced targetSum.
  const remainingSum = targetSum - root.val;
  return hasPathSum(root.left, remainingSum) || hasPathSum(root.right, remainingSum);
}
